const globby = require("globby");
const fs = require("fs");
const nodePlop = require("node-plop");
const plop = nodePlop(`./plopfile.js`);
const generatePackDetails = plop.getGenerator("details");
const jsStringEscape = require("js-string-escape");
const docsLinksfileName = './content-repo/contentItemsDocsLinks.json';

try {
    var docsLinksJson = require(docsLinksfileName);
}
catch (exception) { // in case the reference-docs script was not ran before this one, there will be no links from the marketplace to the reference section.
    var docsLinksJson = {}
}

const contentItemTransformer = {
  integration: "Integrations",
  automation: "Automations",
  playbook: "Playbooks",
  layout: "Layouts",
  layoutscontainer: "Layouts",
  incidenttype: "Incident Types",
  incidentfield: "Incident Fields",
  indicatorfield: "Indicator Fields",
  reputation: "Indicator Types",
  classifier: "Classifiers",
  widget: "Widgets",
  dashboard: "Dashboards",
};

const removeDir = function (path) {
  if (fs.existsSync(path)) {
    const files = fs.readdirSync(path);

    if (files.length > 0) {
      files.forEach(function (filename) {
        if (fs.statSync(path + "/" + filename).isDirectory()) {
          removeDir(path + "/" + filename);
        } else {
          fs.unlinkSync(path + "/" + filename);
        }
      });
      fs.rmdirSync(path);
    } else {
      fs.rmdirSync(path);
    }
  } else {
    console.log("directory path not found.");
  }
};

function capitalizeFirstLetter(string) {
  if (typeof string === "string") {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }
}

function normalizeItemName(itemName) {
  // Removes support level from the name to search the json links file
    const removeFromName = [" (Partner Contribution)", " (Developer Contribution)", " (Community Contribution)", " (beta)", " (Beta)", " (Deprecated)"]

    for (var item of removeFromName) {
        itemName = itemName.replace(item, "")
    }

    return itemName
}

function createReadmeLink(listItem, itemType) {
  // Checks if a readme link for this item exists in the Json file. If not, return an empty string.

  if (!(['integration', 'automation', 'playbook'].includes(itemType))) {
    return ""; // a README file exists only for those entities.
  }

  var normalizedItemName = normalizeItemName(listItem.name);

  if (docsLinksJson[normalizedItemName]) {
    listItem.docLink = docsLinksJson[normalizedItemName]
    }
   else {
    listItem.docLink = ""
  }

  return Promise.resolve();
}

function reverseReleases(obj) {
  let new_obj = {};
  let rev_obj = Object.keys(obj).reverse();
  rev_obj.forEach(function (i) {
    new_obj[i] = obj[i];
  });
  return new_obj;
}

function genPackDetails() {
  let marketplace = [];
  const detailsPages = globby.sync(["./src/pages/marketplace"], {
    absolute: false,
    objectMode: true,
    deep: 1,
    onlyDirectories: true,
  });
  console.log("cleaning up old pack details pages...");
  detailsPages.map((page) => {
    removeDir(page.path);
  });
  console.log("generating new pack details pages");
  const packs = globby.sync(["./index", "!./index/index.json"], {
    absolute: false,
    objectMode: true,
    deep: 1,
    onlyDirectories: true,
  });
  packs.map((pack) => {
    const meta = globby.sync(
      [
        `${pack.path}/metadata.json`,
        `${pack.path}/README.md`,
        `${pack.path}/changelog.json`,
      ],
      {
        absolute: true,
        objectMode: true,
        deep: 1,
      }
    );
    let metadata = JSON.parse(fs.readFileSync(meta[0].path));
    let readme = meta[2] ? meta[1].path : null;
    let changeLog = meta[2]
      ? JSON.parse(fs.readFileSync(meta[2].path, "utf8"))
      : JSON.parse(fs.readFileSync(meta[1].path, "utf8"));
    if (changeLog) {
      for (let [_, release] of Object.entries(changeLog)) {
        release.releaseNotes = jsStringEscape(release.releaseNotes);
        release.released = new Date(release.released).toLocaleString("en-US", {
          year: "numeric",
          month: "long",
          day: "numeric",
        });
      }
    }
    metadata.changeLog = changeLog;
    if (readme) {
      let markdown = fs.readFileSync(readme, "utf8");
      if (markdown == "") {
        metadata.readme = null;
      } else {
        metadata.readme = markdown;
      }
    } else {
      console.log("no README.md for", metadata.name);
    }
    marketplace.push(metadata);
  });

  if (process.env.MAX_PACKS) {
    console.log(`limiting packs to ${process.env.MAX_PACKS}`);
    marketplace = marketplace.slice(0, process.env.MAX_PACKS);
  }

  console.log("writing marketplace metadata to JSON file");
  const marketplace_json = JSON.stringify(marketplace);
  fs.writeFile(
    "index.json",
    marketplace_json,
    "utf8",
    function readFileCallback(err) {
      if (err) {
        console.log(err);
      }
    }
  );


  marketplace.map(async (pack) => {
    const parseContentItems = async () => {
      try {
        if (pack.contentItems) {
          let FixedContentItems = {};
          let fixedKey = ""
          var promises = []
          for (var [key, value] of Object.entries(pack.contentItems)) {
            fixedKey = contentItemTransformer[key];
            for (var listItem of value) {
              listItem.description = listItem.description
                ? jsStringEscape(listItem.description)
                : "";
              listItem.description = listItem.description.replace(/</g, "&#60;");
              promises.push(createReadmeLink(listItem, key));
            }
            FixedContentItems[fixedKey] = value;
          }
          await Promise.all(promises);
          pack.contentItems = FixedContentItems;
        }
      } catch (err) {
        console.log(err);
      }
    }

    await parseContentItems()

    generatePackDetails.runActions({
      id: pack.id ? pack.id.replace(/-|\s/g, "").replace(".", "") : pack.id,
      name: pack.name,
      description: pack.description.replace(/\\/g, "\\\\"),
      author: pack.author,
      currentVersion: pack.currentVersion,
      versionInfo: pack.versionInfo,
      authorImage: pack.authorImage != "" ? pack.authorImage : null,
      readme: pack.readme
        ? jsStringEscape(pack.readme)
        : "",
      support:
        pack.support == "xsoar"
          ? "Cortex XSOAR"
          : capitalizeFirstLetter(pack.support),
      created: new Date(pack.created).toLocaleString("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
      }),
      updated: new Date(pack.updated).toLocaleString("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
      }),
      certification: pack.certification,
      useCases: pack.useCases,
      integrations: pack.integrations,
      contentItems: pack.contentItems,
      changeLog: reverseReleases(pack.changeLog),
    });
  });
};

genPackDetails();

const globby = require("globby");
const fs = require("fs");
const nodePlop = require("node-plop");
const plop = nodePlop(`./plopfile.js`);
const generatePackDetails = plop.getGenerator("details");
const jsStringEscape = require("js-string-escape");
const fetch = require('node-fetch');
const docsLinksfileName = './contentItemsDocsLinks.json';
const docsLinksJson = require(docsLinksfileName);

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

function checkURLAndModifyLink(url, listItem) {
  return fetch(url).then((response) => {
    if (response.ok) {
      listItem.docLink = url;
      docsLinksJson[listItem[name]] = url;
    }
    else {
      listItem.docLink = ""
    }
  }).catch(err => listItem.docLink = "");
}

function normalizeItemName(itemName) {
  // Normalizes the name of the content entity according to the 'normalize_id' method in mdx_utils

  // remove support level from the name to create the link
  var normalizedName = itemName.replace(" (Partner Contribution)", "").replace(" (Developer Contribution)", "").replace(" (beta)", "").replace(" (Beta)", "")

  // split name by upper case letters, replace spaces with dashed and lowercase everything
  normalizedName = normalizedName.split(/(?=[A-Z][a-z])/).join(" ").replace(/\s+/g, '-').toLowerCase();

  // replace all non word characters (dash is ok)
  normalizedName = normalizedName.replace(/[^\w-]/g, "");

  return normalizedName
}

function createReadmeLink(listItem, itemType) {
  // Creates a README link for the relevant entities (include a check if a README exists in the docs)
  if (!(['integration', 'automation', 'playbook'].includes(itemType))) {
    return ""
  }

  var itemName = listItem.name;
  var baseURL = "https://xsoar.pan.dev/docs/reference/"

  var normalizedItemName = normalizeItemName(itemName)

  if (itemType !== "automation") {
    baseURL = baseURL + itemType + "s/" + normalizedItemName
  }

  else {
    baseURL = baseURL + "scripts/" + normalizedItemName
  }

  if (docsLinksJson[itemName]) {
    listItem.docLink = docsLinksJson[itemName]
    return Promise.resolve();
  }

  return checkURLAndModifyLink(baseURL, listItem)
}

function reverseReleases(obj) {
  let new_obj = {};
  let rev_obj = Object.keys(obj).reverse();
  rev_obj.forEach(function (i) {
    new_obj[i] = obj[i];
  });
  return new_obj;
}

async function genPackDetails() {
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


  await Promise.all(marketplace.map(async (pack) => {
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
  }));

  fs.writeFile(docsLinksfileName, JSON.stringify(docsLinksJson), function writeJSON(err) {
    if (err) return console.log(err);
    console.log('writing to ' + docsLinksfileName);
  });
};

genPackDetails();

const globby = require("globby");
const fs = require("fs");
const nodePlop = require("node-plop");
const plop = nodePlop(`./plopfile.js`);
const generatePackDetails = plop.getGenerator("details");
const jsStringEscape = require("js-string-escape");

const contentItemTransformer = {
    "integration": "Integrations",
    "automation": "Automations",
    "playbook": "Playbooks",
    "layout": "Layouts",
    "layoutscontainer": "Layouts",
    "incidenttype": "Incident Types",
    "incidentfield": "Incident Fields",
    "indicatorfield": "Indicator Fields",
    "classifier": "Classifiers",
}

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
    let metadata = require(meta[0].path);
    let readme = meta[2] ? meta[1].path : null;
    let changeLog = meta[2] ? require(meta[2].path) : require(meta[1].path);
    if (changeLog) {
      for (const [key, value] of Object.entries(changeLog)) {
        value.releaseNotes = jsStringEscape(value.releaseNotes);
        value.released = new Date(value.released).toLocaleString("en-US", {
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
    console.log("writing marketplace metadata to JSON file");
    const marketplace_json = JSON.stringify(
      marketplace.slice(0, process.env.MAX_PACKS)
    );
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

    marketplace.slice(0, process.env.MAX_PACKS).map((pack) => {

      if (pack.contentItems) {
        var FixedContentItems = {};
        for (var [key, value] of Object.entries(pack.contentItems)) {
          fixedKey = contentItemTransformer[key]
          for (const listItem of value) {
            listItem.description = jsStringEscape(listItem.description);
            listItem.description = listItem.description.replace("<", "&#60;");
          }
          FixedContentItems[fixedKey] = value
        }
        pack.contentItems = FixedContentItems
      }

      generatePackDetails.runActions({
        id: pack.id.replace(/-|\s/g, "").replace(".", ""),
        name: pack.name,
        description: pack.description.replace(/\\/g, "\\\\"),
        author: pack.author,
        currentVersion: pack.currentVersion,
        versionInfo: pack.versionInfo,
        authorImage: pack.authorImage != "" ? pack.authorImage : null,
        readme: pack.readme
          ? jsStringEscape(pack.readme)
          : `This pack doesn't have any \`README.md\` content yet. If you'd like to contribute click [here](https://github.com/demisto/content/blob/master/Packs/${pack.id}/README.md).`,
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
    return;
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
  marketplace.map((pack) => {

    if (pack.contentItems) {
    var FixedContentItems = {};
      for (var [key, value] of Object.entries(pack.contentItems)) {
        fixedKey = contentItemTransformer[key]
        for (const listItem of value) {
          listItem.description = jsStringEscape(listItem.description);
          listItem.description = listItem.description.replace("<", "&#60;");
        }
        FixedContentItems[fixedKey] = value
      }
      pack.contentItems = FixedContentItems
    }

    generatePackDetails.runActions({
      id: pack.id.replace(/-|\s/g, "").replace(".", ""),
      name: pack.name,
      description: pack.description.replace(/\\/g, "\\\\"),
      author: pack.author,
      currentVersion: pack.currentVersion,
      versionInfo: pack.versionInfo,
      authorImage: pack.authorImage != "" ? pack.authorImage : null,
      readme: pack.readme
        ? jsStringEscape(pack.readme)
        : `This pack doesn't have any \`README.md\` content yet. If you'd like to contribute click [here](https://github.com/demisto/content/blob/master/Packs/${pack.id}/README.md).`,
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
  return;
}

genPackDetails();

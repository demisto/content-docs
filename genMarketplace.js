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

function travelDependenciesJson(firstLvlDepsJson, depsJson, startKey) {
  /* Travels over the dependencies json to create a depdendencies map for each entry starting with startKey like so:
  {
    startKey: {
      mandatory: {
        packName: {
          version: version
        }
      },
      optional: {
        packName: {
          version: version
        }
      },
      version: "...",
      "mandatoryCount": ...,
      "optionalCount": ...
    }
  }
  */
  // don't travel dependencies JSON if already travelled from the startKey
  if (!(startKey in depsJson)) {
    travelDependencies(depsJson, startKey, firstLvlDepsJson);
    depsJson[startKey]['mandatoryCount'] = Object.keys(depsJson[startKey]['mandatory']).length;
    depsJson[startKey]['optionalCount'] = Object.keys(depsJson[startKey]['optional']).length;
  }
}

function travelDependencies(depsJson, startKey, firstLvlDepsJson) {
  // Travel over the dependencies json of a given Pack dependency type, while collecting all sub-dependency mandatory packs
  
  if (!(startKey in depsJson)) {
    if (!(startKey in firstLvlDepsJson)) {
      depsJson[startKey] = {'mandatory': {}, 'optional': {}}
    } else {
      depsJson[startKey] = {...firstLvlDepsJson[startKey]};
    }
  }

  dependencyPacks = depsJson[startKey]['mandatory'];
  for (var depKey in dependencyPacks) {
    if (depsJson[depKey] === undefined) {
      travelDependenciesJson(firstLvlDepsJson, depsJson, depKey);
    }
    
    // fill mandatory sub-dependecies
    for (var subDepKey in depsJson[depKey]['mandatory']) {
      // skip if subDepKey is startKey or if subDepKey is already in node's collected mandatory
      if (subDepKey !== startKey && (dependencyPacks[subDepKey] === undefined) ) {
        if (depsJson[subDepKey] === undefined) {
          // subDepKey wasn't yet traveled
          travelDependenciesJson(firstLvlDepsJson, depsJson, subDepKey);
        }
        // collect subDepKey chained mandatory dependecies (subDepKey incl.)
        for (var chainKey in getMandatoryChainDependencies(subDepKey, depsJson)) {
          depsJson[startKey]['mandatory'][chainKey] = {
            version: depsJson[chainKey].version,
            support: depsJson[chainKey].support === "xsoar" ? "Cortex XSOAR" : capitalizeFirstLetter(depsJson[chainKey].support)
          }
        }
      }
    }
  }
}

function getMandatoryChainDependencies(packName, depsJson, exclusionSet) {
  // collects all mandatory chained dependencies, while skipping over keys it collected along the way

  res = {};
  if (!(packName in depsJson)) {  // sanity
    return res;
  }
  if (exclusionSet === undefined) {
    exclusionSet = new Set(packName);
  }

  for (var depKey in depsJson[packName]['mandatory']) {
    // prevent iterating over a key that was already iterated
    if (!exclusionSet.has(depKey)) {
      exclusionSet.add(depKey);
      res = {
        ...res, 
        ...getMandatoryChainDependencies(depKey, depsJson, exclusionSet)};
        res[packName] = {version: depsJson[packName].version};
    }
  }
  return res
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
  let idToPackMetadata = {};
  const firstLeveldepsMap = {};  // map of dependencies per pack ID (first level)
  const fullDepsJson = {};  // map of dependencies per pack ID (all levels)
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
        }),
        release.version = release.displayName.split(' ')[0];
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
    idToPackMetadata[metadata.id] = {
      version: metadata.currentVersion,
      support: metadata.support === "xsoar" ? "Cortex XSOAR" : capitalizeFirstLetter(metadata.support)
    };
    marketplace.push(metadata);
  });
  console.log("This is the id to pack metadata", idToPackMetadata);
  marketplace.map((metadata) => {
    if (metadata.dependencies) {
      let dependenciesJson = {
        mandatory: {},
        optional: {},
        version: metadata.currentVersion,
        support: metadata.support
      };
      for (var depId in metadata.dependencies) {
        console.log("This is the name", metadata.name);
        console.log("This is the depId", depId);
        let dependency = metadata.dependencies[depId]
        console.log("This is the dependency", dependency);
        if (dependency.mandatory) {
          dependenciesJson["mandatory"][depId] = {
            version: idToPackMetadata[depId].version,
            support: idToPackMetadata[depId].support
          };
        } else {
          dependenciesJson["optional"][depId] = {
            version: idToPackMetadata[depId].version,
            support: idToPackMetadata[depId].support
          };
        }
      }
      firstLeveldepsMap[metadata.id] = dependenciesJson;
    }
  })

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

    await parseContentItems();

    try {
      if (pack.dependencies) {
        if (!(pack.id in fullDepsJson)) {
          travelDependenciesJson(firstLeveldepsMap, fullDepsJson, pack.id)
        }
      }
    } catch (err) {
      console.log(err);
    }

    generatePackDetails.runActions({
      id: pack.id ? pack.id.replace(/-|\s/g, "").replace(".", "") : pack.id,
      packId: pack.id,
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
      licenseLink: pack.hasOwnProperty("eulaLink") ? pack.eulaLink : "https://github.com/demisto/content/blob/master/LICENSE",
      dependencies: fullDepsJson[pack.id],
      premium: pack.hasOwnProperty("premium") ? pack.premium : false
    });
  });
};

genPackDetails();

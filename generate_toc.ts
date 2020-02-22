
import { readFileSync, createReadStream } from 'fs';

const DOCSPREFIX: string='docs'

const sidebars = require('./sidebars');

interface SideBarItem {
	type: "category" | "doc",
	label?: string,
	id?: string,
	tocpath?: string
	items: Array<any>
};

interface Document {
	id: string,
	title: string,
};

function extractFileData(f): Document | undefined {
	// console.log(s)
	let fileName: string = DOCSPREFIX + '/' + f + '.md'
	// console.log(fileName)
	// console.log('opening file ' + fileName)
	let data = readFileSync(fileName,{ encoding: 'utf-8' }).split('\n').filter(Boolean)

	let document: Document = {} as Document;
	if(data[0] === '---' && data[3] === '---') {
		if(data[1].startsWith('id: ')) {
			document.id = data[1].split(': ')[1].trim()
		}
		else document.id = "N/A"
		if(data[2].startsWith('title: ')) {
			document.title = data[2].split(': ')[1].trim()
		}
		else document.title = "N/A"
	}
	return document;
}

function build_toc(tocpath: string, label: string, items: Array<SideBarItem>) {
	let documents: Array<Document> = []
	for(let i of items) {
		// console.log('i is:' + JSON.stringify(i))
		let doc:string = ""
		if(typeof(i) === 'object' && 'type' in i && 'tocpath' in i &&  i.type === "category") {
			build_toc(tocpath + '/' + i.tocpath, label + '/' + i.label, i.items);
			continue;
		}
		else if(typeof(i) === 'object' && 'type' in i && i.type == "doc"){
			doc = i.id;
		}
		else if (typeof(i) === 'string') {
			doc = i;
		}
		else {
			// console.log("Skipping object: " + JSON.stringify(i))
			continue;
		}
		if(doc === tocpath) continue;
		documents.push(extractFileData(doc))
	}

	console.log('Building TOC for label: ' + label + ' with tocpath: ' + DOCSPREFIX + '/' + tocpath + '.md\n' + JSON.stringify(documents) + '\n\n');

}

function parse_sidebars() {
	// console.log(sidebars)
	for(let x in sidebars) {
		build_toc(x, x, sidebars[x])
	}
}

parse_sidebars()


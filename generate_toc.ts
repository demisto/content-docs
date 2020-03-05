import { readFileSync, createReadStream } from 'fs';

const DOCSPREFIX: string='docs'

const sidebars = require('./sidebars');

interface SideBarItem {
	type: "category" | "doc",
	label?: string,
	id?: string,
	items: Array<any>
};

class Document {
	id: string;
	title: string;
	constructor(id?: string, title?: string) {
		this.id = id? id : 'N/A';
		this.title = title? title : 'N/A';
	}
};

class TOC {
	id: string;
	documents: Array<Document>;
	tocs: Array<TOC>;
	constructor(id?: string) {
		this.id = id? id : 'N/A';
		this.documents = new Array<Document>();
		this.tocs = new Array<TOC>();
	}
}

function TOCToMarkDown(toc: TOC, depth: number = 0): string {
	let md: string = "";
	let hashes: string = '#'.repeat(depth+1);
	// title
	md += hashes + ' ' + toc.id[0].toUpperCase() + toc.id.slice(1) + '\n\n';

	// add  all documents first
	for(let doc of toc.documents) {
		md+= '[' + doc.title + ']' + '(' + doc.id + ')\n';
	}

	md+= '\n';

	// ad all TOCs later
	for(let t of toc.tocs) {
		md += TOCToMarkDown(t, depth+1);
	}
	
	return md;
}

function extractFileData(f): Document | undefined {
	// console.log(s)
	let fileName: string = DOCSPREFIX + '/' + f + '.md'
	// console.log(fileName)
	// console.log('opening file ' + fileName)
	let data = readFileSync(fileName,{ encoding: 'utf-8' }).split('\n').filter(Boolean)

	let document: Document = new Document();

	if(data[0] === '---' && data[3] === '---') {
		if(data[1].startsWith('id: ')) {
			document.id = data[1].split(': ')[1].trim()
		}
		if(data[2].startsWith('title: ')) {
			document.title = data[2].split(': ')[1].trim()
		}
	}
	return document;
}

function build_toc(label: string, items: Array<SideBarItem>): TOC {
	let toc : TOC = new TOC(label);
	toc.id = label;

	for(let i of items) {

		// element is a category: add it as a new TOC
		if(typeof(i) === 'object' && 'type' in i && i.type === "category") {
			toc.tocs.push(build_toc(label + '/' + i.label, i.items));
		}

		// element is a document: add is as a new Document
		else if(typeof(i) === 'object' && 'type' in i && i.type == "doc"){
			toc.documents.push(extractFileData(i.id))
		}

		// element is a string: add it as a document
		else if (typeof(i) === 'string') {
			toc.documents.push(extractFileData(i))
		}
		// skip something unknown
		else {
			// console.log("Skipping object: " + JSON.stringify(i))
			continue;
		}
	}
	// console.log('Building TOC for label: ' + label + '\n' + JSON.stringify(toc.documents) + '\n\n');
	return toc;
}

function parse_sidebars() {
	// console.log(sidebars)
	let toc: TOC = undefined;
	for(let x in sidebars) {
		toc = build_toc(x, sidebars[x])
		// console.log('TOC for sidebar ' + x + ' is: ' + JSON.stringify(toc))
		console.log(TOCToMarkDown(toc))
	}
}

parse_sidebars()


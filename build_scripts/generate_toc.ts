import { readFileSync, existsSync, lstatSync, writeFileSync } from 'fs';

interface SideBarItem {
	type: 'category' | 'doc',
	label?: string, // categories have label
	id?: string, // documents have id
	items: Array<any>
};

class Document {
	id: string; // id of the document as shown in the sidebar
	title: string;
	path: string; // path of the document relative to the docs root
	constructor(id?: string, title?: string, path?: string) {
		this.id = id? id : 'N/A';
		this.title = title? title : 'N/A';
		this.path = path? path : './';
	}
};

class TOC {
	label: string;
	documents: Array<Document>;
	tocs: Array<TOC>;
	path: string;
	constructor(label?: string, path?: string) {
		this.label = label? label : 'N/A';
		this.path = path? path : './';
		this.documents = new Array<Document>();
		this.tocs = new Array<TOC>();
	}
}

function TOCToMarkDown(toc: TOC, depth: number = 0): string {
	let md: string = '';
	let hashes: string = '#'.repeat(depth+1);
	let topic: string = toc.label.split('/').pop()
	if(depth == 0) { // if main TOC, just build metadata
		md += '---\n';
		md += 'id: ' + topic + '\n';
		md += 'title: ' + topic[0].toUpperCase() + topic.slice(1) + '\n';
		md += '---\n';
	}
	else { // else build header
		md += hashes + ' ' + topic[0].toUpperCase() + topic.slice(1) + '\n\n\n';
	}

	// add  all documents first 
	for(let doc of toc.documents) {
		if(doc.id === topic) continue; // skip self
		md+= '- [' + doc.title + ']' + '(' + doc.path + ')\n\n';
	}

	md+= '\n';

	// ad all TOCs later
	for(let t of toc.tocs) {
		md += TOCToMarkDown(t, depth+1);
	}
	
	return md;
}

function extractFileData(documentName: string, docsRoot: string, docPath: string): Document | undefined {
	// filename is relative to where the script runs
	let fileName: string = docsRoot + '/' + documentName + '.md'
	let documentPath: string = docPath  + documentName
	let data = readFileSync(fileName,{ encoding: 'utf-8' }).split('\n').filter(Boolean)

	let document: Document = new Document();

	// document.path is relative to the content root directory
	document.path = documentPath;

	// TODO: improve the parsing here in case additional metadata is added and more lines are present
	if(data[0] === '---' && data[3] === '---') {
		if(data[1].startsWith('id: ')) {
			document.id = data[1].split(': ')[1].trim()
		}
		if(data[2].startsWith('title: ')) {
			document.title = data[2].split(': ')[1].trim()
		}
	}
	else throw new Error('Cannot parse metadata for document: ' + fileName);
	return document;
}

function build_toc(label: string, items: Array<SideBarItem>, docsRoot: string, docPath: string): TOC {
	let toc : TOC = new TOC(label,docPath);

	for(let item of items) {

		// element is a category: add it as a new TOC
		if(typeof(item) === 'object' && 'type' in item && item.type === 'category') {
			let subLabel: string = label + '/' + item.label;
			toc.tocs.push(build_toc(subLabel, item.items, docsRoot, docPath));
		}

		// element is a document: add is as a new Document
		else if(typeof(item) === 'object' && 'type' in item && item.type == 'doc'){
			toc.documents.push(extractFileData(item.id, docsRoot, docPath))
		}

		// element is a string: add it as a document
		else if (typeof(item) === 'string') {
			toc.documents.push(extractFileData(item, docsRoot, docPath))
		}
		// skip something unknown
		else {
			// console.log('Skipping object: ' + JSON.stringify(i))
			continue;
		}
	}
	// console.log('Building TOC for label: ' + label + '\n' + JSON.stringify(toc.documents) + '\n\n');
	return toc;
}

function main(args: Array<string>) {
	args = args.splice(2)
	if(args.length != 5) {
		console.log('Error! Usage is: generate_toc [sidebarfile] [sidebarname] [docsRoot] [docPath] [outputfile]');
		console.log('[sidebarfile] is the sidebar.js file relative to your current path');
		console.log('[sidebarname] is the name of the sidebar as defined in the sidebars.js file');
		console.log('[docsRoot] is filesystem path of the docs folder relative to your current path');
		console.log('[docPath] is the root path of the docs relative to the web site (i.e. /docs/)');
		console.log('[outputfile] is the markdown file to write the TOC in, relative to your current path');
		return;
	}

	const sidebarFile: string = args[0];
	const sidebarName: string = args[1]
	const docsRoot: string = args[2];
	const docPath: string = args[3];
	const outputFile: string = args[4];

	try {

		// check if the sidebars file exist and import it
		if(!existsSync(sidebarFile)) throw new Error('Sidebar file doesn\'t exist!');
		const sidebars = require(sidebarFile);
		// check if sidebar name exists in sidebars
		let sidebar: Array<SideBarItem> = undefined;
		if(sidebarName in sidebars) {
			sidebar = sidebars[sidebarName]
		}
		else throw new Error('Sidebar ' + sidebarName + ' does not exist in sidebars!')

		// check if the docs root exist and is a directory
		if(!existsSync(docsRoot)) throw new Error('Document root directory doesn\'t exist!');
		if(!lstatSync(docsRoot).isDirectory()) throw new Error('Document root is not a directory!');

		// check if the sidebar docs root exists and is a directory
		let sidebarRootDir = docsRoot + '/' + sidebarName
		if(!existsSync(sidebarRootDir)) throw new Error('Sidebar root directory doesn\'t exist!');
		if(!lstatSync(sidebarRootDir).isDirectory()) throw new Error('Sidebar root is not a directory!');
			
		let toc : TOC = build_toc(sidebarName, sidebars[sidebarName], docsRoot, docPath)
		let md: string = TOCToMarkDown(toc);
		// write the file
		writeFileSync(outputFile, md);
		console.log('TOC created for:', sidebarName, 'in', outputFile);
		// console.log(md);
	} catch(err) {
		console.error('Error:', err);
		return;
	}
}

main(process.argv)
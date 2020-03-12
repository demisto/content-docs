import {  readdirSync, readFileSync, lstatSync } from 'fs';

const DOCSPREFIX: string='docs'

class Document {
	id: string;
	title: string;
    path: string;
    section: string;
	constructor(id?: string, title?: string, path?: string, section?: string) {
		this.id = id? id : 'N/A';
		this.title = title? title : 'N/A';
        this.path = path? path : '/';
        this.section = section? section: 'N/A'
	}
};

interface SideBarDoc {
	type: string,
	id: string
}

interface SideBarElement {
	type: 'category' | 'doc',
	label: string,
	items: Array<string | SideBarDoc | SideBarElement>
}

class TOC {
	id: string;
	documents: Array<Document>;
	tocs: Array<TOC>;
	path: string;
	constructor(id?: string, path?: string) {
		this.id = id? id : 'N/A';
		this.path = path? path : '/';
		this.documents = new Array<Document>();
		this.tocs = new Array<TOC>();
	}
}

function TOCToSideBar(toc: TOC, depth: number = 0): SideBarElement {
	let SideBar: SideBarElement = {
		type: 'category',
		label: toc.id,
		items: new Array()
	}

	// add  all documents first
	for(let doc of toc.documents) {
		let d: SideBarDoc | string = undefined;
		if(depth == 0) {
			d = {
				type: "doc",
				id: doc.id
			}
		}
		else {
			d= doc.id
		}
		SideBar.items.push(d)
	}

	// ad all TOCs later
	for(let t of toc.tocs) {
		SideBar.items.push(TOCToSideBar(t, depth+1))
	}
	
	return SideBar;
}

function extractFileData(f): Document | undefined {
	// console.log(s)
	let fileName: string = f;
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

function generate_sidebar(path:string) {
  	let toc : TOC = new TOC(path, path);

    let entries = readdirSync(path);
    
    for(let entry of entries) {
        let fullPath: string = path + '/' + entry;
        let fileInfo = lstatSync(fullPath);
        // console.log(fullPath);
        if(fileInfo.isDirectory()) {
            toc.tocs.push(generate_sidebar(fullPath))
        }
        else if(entry.toLowerCase().endsWith('.md')) {
            toc.documents.push(extractFileData(fullPath));
        }
        else {
            // console.log('skipping file: ' + fullPath)
        }
    }   
    return toc;

 }
 
let toc: TOC = generate_sidebar(DOCSPREFIX + "/" + 'reference');
console.log(JSON.stringify(TOCToSideBar(toc)))

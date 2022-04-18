const visit = require('unist-util-visit')
const fs = require('fs')
const path = require('path')

const mdxEditor = (options) => {
  const handlePaths = (filePath, newName, importsList, text, workingDir) => {
    var absolutePath = path.join(workingDir,filePath);
    if (fs.existsSync(absolutePath)) {
      const importLine = `import ${newName} from '!!raw-loader!${absolutePath}';`
      importsList.push(importLine)
      const newText = text.replace(`'${filePath}'`, `{${newName}}`)
      return newText
    } else {
      return text
    }
  }
  const createNewText = (text, counter, importsList, workingDir) => {
    const orgStart = text.indexOf("'") + 1
    const orgEnd = text.indexOf("'", orgStart)
    const solStart = text.indexOf("'", orgEnd + 1) + 1
    const solEnd = text.indexOf("'", solStart)

    const orgPath = text.substring(orgStart, orgEnd)
    const solPath = text.substring(solStart, solEnd)

    const orgName = 'org_'.concat(counter.toString())
    const solName = 'sol_'.concat(counter.toString())

    let newText = handlePaths(orgPath, orgName, importsList, text, workingDir)
    newText = handlePaths(solPath, solName, importsList, newText, workingDir)
    return newText
  }

  const transformer = async (ast, vfile) => {
    let counter = 0
    const importsArr= []
    let mdSyntexFound = false
    visit(
      ast,
      { type: 'code', lang: 'LearningEditor' },
      (node, index, parent) => {
        const newText = createNewText(node.value, counter, importsArr, vfile.dirname)
        parent.children.splice(index, 1, {
          type: 'jsx',
          value: `<LearningEditor ${newText} />`,
          position: node.position
        })
        mdSyntexFound = true
        counter = counter + 1
      }
    )
    if (mdSyntexFound) {
      importsArr.push(
        "import { LearningEditor } from './../../editor-plugin/LearningEditor.js';"
      )
    }
    for (let i = 0; i < importsArr.length; i++) {
      ast.children.splice(0, 0, {
        type: 'import',
        value: importsArr[i]
      })
    }
  }
  return transformer
}

module.exports = mdxEditor

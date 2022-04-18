import React, { lazy, useState, useRef, Suspense } from 'react'
import PropTypes from 'prop-types'
import style from './style.module.css'

const MonacoEditor = lazy(() => import('react-monaco-editor'))
const MonacoDiffEditor = lazy(() => import('react-monaco-editor/lib/diff'))

const Button = ({ onClick, text }) => {
  return (
    <button className={style.navButtons} onClick={onClick}>
      {text}
    </button>
  )
}

const DiffButton = ({ onClick, text }) => {
  return (
    <button className={style.navDiffButtons} onClick={onClick}>
      {text}
    </button>
  )
}

DiffButton.propTypes = {
  onClick: PropTypes.func.isRequired,
  text: PropTypes.string
}

Button.propTypes = {
  onClick: PropTypes.func.isRequired,
  text: PropTypes.string
}

const EditorButtons = ({
  OrgFunction,
  SolutionFunction,
  DifferenceFunction
}) => (
  <div>
    <div className={style.editorBar}>
      <Button onClick={OrgFunction} text="&#x1F6E0; Your code"></Button>
      <Button onClick={SolutionFunction} text="&#x2705; Solution"></Button>
      <DiffButton
        onClick={DifferenceFunction}
        text="&#x1D321; Difference"
      ></DiffButton>
    </div>
  </div>
)

EditorButtons.propTypes = {
  OrgFunction: PropTypes.func.isRequired,
  SolutionFunction: PropTypes.func.isRequired,
  DifferenceFunction: PropTypes.func.isRequired
}

export const LearningEditor = (props) => {
  const [UserText, setUserText] = useState(props.original)
  const [CurText, setCurText] = useState(props.original)
  const [IsDiffEditor, setDiffEditor] = useState(false)

  const editorLanguage = props.language ? props.language : 'python'

  const editorRef = useRef(null)

  const OnOrgClick = () => {
    setUserText(UserText)
    setCurText(UserText)
    setDiffEditor(false)
  }

  const OnSolutionClick = () => {
    // if we arrived from Code view keep value, if we arrived from Difference keep old value
    const NewUserText = !IsDiffEditor ? editorRef.current.getValue() : UserText

    setUserText(NewUserText)
    setCurText(props.solution)
    setDiffEditor(false)
  }

  const OnDifferenceClick = () => {
    // if we arrived from Code view keep value, if we arrived from Solution keep old value
    const NewUserText =
      CurText !== props.solution ? editorRef.current.getValue() : UserText

    setUserText(NewUserText)
    setCurText(CurText)
    setDiffEditor(true)
  }

  const handleEditorDidMount = (editor) => {
    editorRef.current = editor
  }

  const handleEditorUnmount = () => {
    console.log('unmount')
  }

  const GetEditor = () => {
    return (
      <MonacoEditor
        height="400"
        language={editorLanguage}
        value={CurText}
        theme="vs-dark"
        editorDidMount={handleEditorDidMount}
        editorWillUnmount={handleEditorUnmount}
      />
    )
  }

  const GetDiffEditor = () => {
    return (
      <MonacoDiffEditor
        height="400"
        language={editorLanguage}
        value={props.solution}
        original={UserText}
        theme="vs-dark"
        editorDidMount={handleEditorDidMount}
        editorWillUnmount={handleEditorUnmount}
      />
    )
  }

  return (
    <Suspense fallback={<div></div>}>
      <div>
        {IsDiffEditor ? GetDiffEditor() : GetEditor()}
        <EditorButtons
          OrgFunction={OnOrgClick}
          SolutionFunction={OnSolutionClick}
          DifferenceFunction={OnDifferenceClick}
        ></EditorButtons>
      </div>
    </Suspense>
  )
}

LearningEditor.propTypes = {
  original: PropTypes.string,
  solution: PropTypes.string,
  language: PropTypes.string
}

function Frame1(props) {

  return (
    <div className="content">
      <span>Frame 1</span>
      <button onClick={props.next}>Next Frame</button>
    </div>
  )
}

export default Frame1;
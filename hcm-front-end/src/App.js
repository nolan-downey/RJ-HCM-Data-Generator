import { Fragment, useState } from "react";
import './App.css';
import Nav from "./nav";
import Frame0 from "./frame0"
import Frame1 from "./frame1"
import Frame2 from "./frame2"

function App() {

  const [frame, nextFrame] = useState(0);
  const [table, setTable] = useState("");

  return (
    <Fragment>
      <Nav/>
       {/* Package each page content into different functions in other files */}
      {frame === 0 && <Frame0 next={() => nextFrame(1)}/>}
      {frame === 1 && <Frame1 selectTable={table => setTable(table)} next={() => nextFrame(2)}/>}
      {frame === 2 && <Frame2 table={table}/>}
    </Fragment>
  )
}

export default App;
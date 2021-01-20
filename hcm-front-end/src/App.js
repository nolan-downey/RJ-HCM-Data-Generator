import { Fragment, useState } from "react";
import './App.css';
import TestingEndpoint from './TestingEndpoint';

function App() {

  const [frame, nextFrame] = useState(0);
  const [table, setTable] = useState("");

  return (
<<<<<<< HEAD
    <Fragment>
      <Nav/>
       {/* Package each page content into different functions in other files */}
      {frame === 0 && <Frame0 next={() => nextFrame(1)}/>}
      {frame === 1 && <Frame1 selectTable={table => setTable(table)} next={() => nextFrame(2)}/>}
      {frame === 2 && <Frame2 table={table}/>}
    </Fragment>
=======
    <div className="App"> 
      <header className="App-header">
        <TestingEndpoint endPoint={"jobApplicants"} spikingValues={[0, 20, 40]}/>
        {/* <label htmlFor="state" style={{display: 'block'}}>
          Choose a database and state whose addresses you want to view
        </label>
        <select name="dbNames" onChange={handleChangeDB}>
          {dbs && Array.isArray(dbs) ? 
            dbs.length > 0 ? 
              dbs.map((db, idx) => (
                <option key={idx} value={db}>
                  {db}
                </option>))
              : <> ... </>
            : <> </>}
        </select>
        <select name="states" onChange={getStateCode}>
          {STATENAMES.map((state, idx) => <option key={idx} value={state}>{state}</option>)}
        </select>
          {states && Array.isArray(states) ? 
            states.length > 0 ? 
              states.map((state, idx) => (
                <span key={idx} style={{display: 'block'}}>
                  Address {idx}: {state.cityName}, {state.stateCode} {state.countryCode}
                </span>))
              : <>...</>
            : <>...</>} */}
      </header>
    </div>
>>>>>>> testing endpoint page
  )
}

export default App;
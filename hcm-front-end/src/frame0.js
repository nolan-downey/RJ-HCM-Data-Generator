import { useEffect, useRef, useState } from 'react';
import { APIURL, STATENAMES } from './literals';
import axios from 'axios';

function Frame0(props) {

  const [states, setStates] = useState();
  const [dbs, setDbs] = useState();
  
  const getStateCode = (selection) => {
    if (typeof(selection) !== 'string')
      selection = selection.target.value;
    axios.get(`${APIURL}/api/addresses?stateCode=${selection}`)
      .then(response => {
        setStates(response.data || 'No addresses');
      })
      .catch(error => {
        setStates(error);
      });
  }

  const handleChangeDB = (selection) => {
    selection = selection.target.value;
    axios.post(`${APIURL}/api/changeDB`, {"dbName": selection})
      .then(response => {
        console.log(response);
      })
      .catch(error => {
        console.log(error);
      })
  }

  const getDBNames = useRef(() => {})
  getDBNames.current = () => {
    axios.get(`${APIURL}/api/getdbnames`)
      .then(response => {
        setDbs(response.data || 'No dbs');
      })
      .catch(error => {
        setDbs(error);
      });
  };

  useEffect(() => {
    getStateCode(STATENAMES[0]);
    getDBNames.current();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <label htmlFor="state" style={{display: 'block'}}>
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
        <button className="next-frame" onClick={props.next}>Continue</button>
      </header>
    </div>
  )
}

export default Frame0;
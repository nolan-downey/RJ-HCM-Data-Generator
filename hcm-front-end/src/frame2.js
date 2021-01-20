import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import { APIURL } from './literals';
import Loader from './Loader';

function Frame2({ table, previous }) {
  const [loadedData, setLoadedData] = useState(false);
  const [fetchingData, setFetchingData] = useState(false);
  const [data, setData] = useState();

  const determineTable = (tableString) => {
    switch(tableString) {
      case "Address":
        return "address";
      case "Person":
        return "person";
      case "Worker":
        return "worker";
      case "Job Applicant":
        return "jobApplicant";
      case "Job Requisition":
        return 'jobRequisition';
      default:
        return "";
    }
  }

  const fetchJobApplicant = (selection) => {
    setLoadedData(false);
    setFetchingData(true);
    selection = determineTable(selection)
    axios.get(`${APIURL}/api/${selection}`)
      .then(res => {
        if (res) {
          setLoadedData(true);
          setData(JSON.stringify(JSON.parse(res.data), null, 2));
        }
      })
      .catch(err => {
        setLoadedData(true);
        setData(JSON.stringify(err));
      })
      .finally(() => setFetchingData(false))
  }

  return (
    <div className="testingMainView">
      <div className="spikingMenu">
        Spiking Menu
        <div style={{positon: "absolute"}}>
          <button onClick={() => fetchJobApplicant(table)}>Fetch Data</button>
        </div>
      </div>
      <div className="responseView">
        Sample Response 
      {
        fetchingData ? <Loader/> 
          : loadedData ? 
              <div className="responseWindow">
                <pre>
                  {data}
                </pre>
              </div>
          : <div>...</div>
      }
      </div>
      <button className="next-frame" onClick={previous}>Previous Frame</button>
    </div>
  )
}

export default Frame2;
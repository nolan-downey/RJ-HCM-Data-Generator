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

  const fetchData = (selection) => {
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
    <div className="content">
      <div className="testingMainView">
        <div className="spikingMenu">
          <h1>Spiking Menu</h1>
          <ul>
          {/* Spiking options here */}
          </ul>
          <div style={{positon: "absolute"}}>
            <button onClick={() => fetchData(table)}>Fetch Data</button>
          </div>
        </div>
        <div className="responseView">
          <h1>Sample Response</h1>
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
      </div>
      <button className="next-frame" onClick={previous}>Back</button>
    </div>
  )
}

export default Frame2;
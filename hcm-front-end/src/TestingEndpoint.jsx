import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './testingEndpoint.css';
import { APIURL } from './literals';
import Loader from './Loader';

const TestingEndpoint = ({ endPoint, spikingValues }) => {
  const [loadedData, setLoadedData] = useState(false);
  const [fetchingData, setFetchingData] = useState(false);
  const [data, setData] = useState();

  useEffect(() => {
    console.log(spikingValues);
  }, [spikingValues])

  const fetchJobApplicant = (selection) => {
    setLoadedData(false);
    setFetchingData(true);
    selection = selection.target.value;
    axios.get(`${APIURL}/api/${endPoint}`)
      .then(res => {
        if (res) {
          setLoadedData(true);
          setData(JSON.stringify(JSON.parse(res.data), null, 2));
        }
      })
      .catch(err => {
        setLoadedData(true);
        setData(err);
      })
      .finally(() => {
        setFetchingData(false)
      })
  }

  return (
    <div className="testingMainView">
      <div className="spikingMenu">
        Spiking Menu
        <div style={{positon: "absolute"}}>
          <button onClick={fetchJobApplicant}>Fetch Data</button>
        </div>
      </div>
      <div className="responseView">
        Sample Response 
      {
        fetchingData ? <Loader/> : 
        loadedData ? 
            <div className="responseWindow">
              <pre>
                {data}
              </pre>
            </div>
        : <div>...</div>
      }
      </div>
    </div>
  )
}

export default TestingEndpoint;
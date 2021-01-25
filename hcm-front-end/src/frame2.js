import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import { APIURL } from './literals';
import Loader from './Loader';

function Frame2({ table, previous }) {
  const [loadedData, setLoadedData] = useState(false);
  const [fetchingData, setFetchingData] = useState(false);
  const [data, setData] = useState();

  // Spike options state
  const [companyName, newName] = useState("");
  const [state, newState] = useState("");
  const [city, newCity] = useState("");
  const [age, newAge] = useState({});
  const [ethnicity, newEthnicity] = useState({});
  const [gender, newGender] = useState({});
  const [workerTypes, newWorkerTypes] = useState({});
  const [fullTimeEquivalency, newFullTimeEquivalency] = useState({});

  let spikeOptions = (
    <ul className="spikeList">
      <li>Company Name<input onChange={e => newName(e.target.value)}></input></li>
      <li>State<input onChange={e => newState(e.target.value)}></input></li>
      <li>City<input onChange={e => newCity(e.target.value)}></input></li>
      {/* <li>Age<input onChange={e => newAge(e.target.value)}></input></li> */}
      <li className="colHeader">Age (%)
        <ul className="spikeList">
          <li>20's<input onChange={e => {
            let temp = age
            temp["20"] = e.target.value
            newAge(temp)
          }}></input></li>
          <li>30's<input onChange={e => {
            let temp = age
            temp["30"] = e.target.value
            newAge(temp)
          }}></input></li>        
          <li>40's<input onChange={e => {
            let temp = age
            temp["40"] = e.target.value
            newAge(temp)
          }}></input></li>
          <li>50's<input onChange={e => {
            let temp = age
            temp["50"] = e.target.value
            newAge(temp)
          }}></input></li> 
          <li>60+<input onChange={e => {
            let temp = age
            temp["60"] = e.target.value
            newAge(temp)
          }}></input></li>             
        </ul>
      </li> 
      {/* <li>Ethnicity<input onChange={e => newEthnicity(e.target.value)}></input></li> */}
      <li className="colHeader">Ethnicity (%)
        <ul className="spikeList">
          <li>Non-Hispanic/Latino White<input onChange={e => {
            let temp = ethnicity
            temp["Non-Hispanic/Latino White"] = e.target.value
            newEthnicity(temp)
          }}></input></li>
          <li>Pacific Islander<input onChange={e => {
            let temp = ethnicity
            temp["Pacific Islander"] = e.target.value
            newEthnicity(temp)
          }}></input></li>        
          <li>Native American<input onChange={e => {
            let temp = ethnicity
            temp["Native American"] = e.target.value
            newEthnicity(temp)
          }}></input></li>
          <li>Asian (Non-Hispanic/Latino)<input onChange={e => {
            let temp =  ethnicity
            temp["Asian (Non-Hispanic/Latino)"] = e.target.value
            newEthnicity(temp)
          }}></input></li> 
          <li>Non-white Hispanic/Latino<input onChange={e => {
            let temp =  ethnicity
            temp["Non-white Hispanic/Latino"] = e.target.value
            newEthnicity(temp)
          }}></input></li> 
          <li>African or African American (Non-Hispanic/Latino)<input onChange={e => {
            let temp = ethnicity
            temp["African or African American (Non-Hispanic/Latino)"] = e.target.value
            newEthnicity(temp)
          }}></input></li> 
        </ul>
      </li>  
      <li className="colHeader">Gender (%)
        <ul className="spikeList">
          <li>Male<input onChange={e => {
            let temp = gender
            temp["male"] = e.target.value
            newGender(temp)
          }}></input></li>
          <li>Female<input onChange={e => {
            let temp = gender
            temp["female"] = e.target.value
            newGender(temp)
          }}></input></li>        
          <li>Other<input onChange={e => {
            let temp = gender
            temp["other"] = e.target.value
            newGender(temp)
          }}></input></li>            
        </ul>
      </li>
      <li className="colHeader">Worker Type (%)
        <ul className="spikeList">
          <li>Employee<input onChange={e => {
            let temp = workerTypes
            temp["employee"] = e.target.value
            newWorkerTypes(temp)
          }}></input></li>
          <li>Contract<input onChange={e => {
            let temp = workerTypes
            temp["contract"] = e.target.value
            newWorkerTypes(temp)
          }}></input></li>              
          <li>Temporary<input onChange={e => {
            let temp = workerTypes
            temp["temporary"] = e.target.value
            newWorkerTypes(temp)
          }}></input></li>            
        </ul>
      </li>
      {/* <li>Time Status<select onChange={e => newFullTimeEquivalency(e.target.value)}></select></li> */}
      <li className="colHeader">Full Time / Part Time (%)
        <ul className="spikeList">
          <li>Part Time<input onChange={e => {
            let temp = fullTimeEquivalency
            temp["partTime"] = e.target.value
            newFullTimeEquivalency(temp)
          }}></input></li>
          <li>Full Time<input onChange={e => {
            let temp = fullTimeEquivalency 
            temp["fullTime"] = e.target.value
            newFullTimeEquivalency(temp)
          }}></input></li>        
        </ul>
      </li>
    </ul>
  )

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

  const fetchData = async (selection) => {
    setLoadedData(false);
    setFetchingData(true);

    // Grab spiked fields from HTML
    let data = {
      companyName: companyName === "" ? "" : companyName,
      addrInfo: {state: state === "" ? "" : state, city: city === "" ? "" : city},
      age: age === "" ? 0 : age,
      ethnicity: ethnicity === "" ? "" : ethnicity,
      gender: gender === "" ? "" : gender,
      workerTypes: workerTypes === {} ? "" : workerTypes, // Employee, Temp, Contractor
      fullTimeEquivalency: fullTimeEquivalency === "" ? "" : fullTimeEquivalency // Full Time, Part Time
    }

    // Create new DB with spiked fields
    await axios.post(`${APIURL}/api/newDB`, data)
    .then(res => {
      console.log(res)
    })
    .catch(err => {
      console.log(err)
    })

    selection = determineTable(selection)
    await axios.get(`${APIURL}/api/${selection}`)
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
          {spikeOptions}
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
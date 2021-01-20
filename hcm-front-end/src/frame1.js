import { useState } from "react";

function Frame1(props) {
  const [active, setActive] = useState("");

  function handleUpdate(table) {
    setActive(table);
    props.selectTable(table);
  }

  return (
    <div className="content">
      <div className="table-menu">
        <button className={active === "Address" ? "selected" : "unselected"} onClick={() => handleUpdate("Address")}>Address</button>
        <button className={active === "Person" ? "selected" : "unselected"} onClick={() => handleUpdate("Person")}>Person</button>
        <button className={active === "Worker" ? "selected" : "unselected"} onClick={() => handleUpdate("Worker")}>Worker</button>
        <button className={active === "Job Applicant" ? "selected" : "unselected"} onClick={() => handleUpdate("Job Applicant")}>Job Applicant</button>
        <button className={active === "Job Requisition" ? "selected" : "unselected"} onClick={() => handleUpdate("Job Requisition")}>Job Requisition</button>
      </div>
      {active !== "" && <button className="next-frame" onClick={props.previous}>Previous Frame</button>}
      {active !== "" && <button className="next-frame" onClick={props.next}>Next Frame</button>}
    </div>
  )
}

export default Frame1;
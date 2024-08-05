import React from "react";
import axios from "axios";


function App() {
  var [user,setUser] = React.useState('');
  var [pass,setPass] = React.useState('');
  var [enter,setEnter] = React.useState(false);
  var [arr,setArr] = React.useState([]);
  // var arr = [];
  function userChange(event){
    setUser(event.target.value)
  }
  function passChange(event){
    setPass(event.target.value)
  }
  async function formSubmit(event){
    event.preventDefault();
    await axios.get("http://localhost:8090/api/notes/",{
      params:{
      mainuser:user,
      mainpass:pass,
      }
    },{
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    }).then((res)=>{
        setArr(res.data)
        console.log(arr[0]);
        setEnter(true)
    })
    .catch((e)=>{
      setArr([])
      setEnter(true)})
  }

  var [user1,setUser1] = React.useState("");
  var [pass1,setPass1] = React.useState("");
  var [msg,setMsg] = React.useState("");
  function user1Change(event){
    setUser1(event.target.value)
  }
  function pass1Change(event){
    setPass1(event.target.value)
  }
  function msgChange(event){
    setMsg(event.target.value)
  }
  async function dataSubmit(event){
    event.preventDefault();
    await axios.post("http://localhost:8090/api/notes/",JSON.stringify({
      mainuser:user,
      mainpass:pass,
      username:user1,
      password:pass1,
      description:msg
    }),{
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    }).then((res)=>{
      console.log(res.data)
      setEnter(false)
    })
    .catch((err)=>console.log(err))
    setUser("")
    setPass("")
    setUser1("")
    setPass1("")
    setMsg("")
  }

  return(
  (!enter) ?<div id="backid">
    <h1>Password Safe</h1>
    <h3>Just remember one username and password, we will remember all your credentials</h3>
    <form onSubmit={formSubmit}>
      <label htmlFor="userid" className="user">Enter Username</label>
      <input required type="text" placeholder="Enter username" id="userid" name="userid" value={user} onChange={userChange} /><br/><br/>
      <label htmlFor="passid" className="user">Enter password</label>
      <input required type="password" placeholder="Enter Password" id="passid" name="passid" value={pass} onChange={passChange} /><br/><br/>
      <button type="submit"  id="submitid">submit</button>
    </form>
  </div>
  :<div id="t1">
  <div id="t2">
    {arr.map(item=>(
      <div className="c1">
      <p className="c2">username:{item.username}</p>
      <p className="c3">password:{item.password}</p>
      <p className="c4">description:{item.description}</p>
      </div>))}
  </div>
  <form onSubmit={dataSubmit} id="t8">
    <h1 id="t3">Enter details to be stored</h1>
    <label id="t4" htmlFor="userid1">Enter username</label>
    <input required type="text" placeholder="Enter username" id="userid1" name="userid1" value={user1} onChange={user1Change} />
    <label id="t5" htmlFor="passid1">Enter password</label>
    <input required type="password" placeholder="Enter Password" id="passid1" name="passid1" value={pass1} onChange={pass1Change} />
    <label id="t6" htmlFor="msgid">Enter message</label>
    <input type="text" placeholder="Enter message" id="msgid" name="msgid" value={msg} onChange={msgChange} />
    <button id="t7" type="submit">submit</button>
  </form>
</div>
  )
}

export default App;

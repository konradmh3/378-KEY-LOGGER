//the below function gets the log file and updates the p tag with 
//the contents of the log file
    
function updateLog(){
    // fetch the log file
    fetch('static/log.txt')
    .then(response => response.text())
    .then(data => {
        // get the p tag with id "log"
        const p = document.getElementById('log');
        // set the p tag text to the contents of the log file
        p.innerText = data;
    })
}
    // call the updateLog function every 2.5 secocd nds
setInterval(updateLog, 5000);

    

//this below function adds a route for the server and updates 
//the log file with an empty string in the server
function clearLog(){
    // make a post request to the clearLog route
    fetch('/clearLog', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        // if the success key is true
        if(data.success){
            // update the log
            updateLog();
        }
    })
}

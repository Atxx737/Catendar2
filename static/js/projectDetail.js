var numTask= document.querySelector(".nu-task");
<<<<<<< HEAD
console.log("numTask",numTask);


var numTaskDone= document.querySelector(".nu-taskdone");

var incomplete= numTask.value- numTaskDone.value;
=======
console.log("numTask",numTask.value);


var numTaskDone= document.querySelector(".nu-taskdone");
console.log("numTaskDone",numTaskDone.value);
    

var incomplete= numTask.value - numTaskDone.value;
console.log("incomplete",incomplete);
>>>>>>> new_brach
    
    
window.onload = function () {
var data = [numTaskDone.value,incomplete ];
<<<<<<< HEAD
var labels = ['Compelete','Incomple' ];
=======
var labels = ['Compelete','Incomplete' ];
>>>>>>> new_brach

var config = {
    type: 'doughnut',
    data: {
    labels: labels,
    datasets: [
        {
<<<<<<< HEAD
        label: 'Incomple',
        backgroundColor: [
        '#D8E9A8',
=======
        label: 'Compelete',
        backgroundColor: [
        'rgba(74, 169, 108)',
>>>>>>> new_brach
        'rgba(249, 151, 93)',
        ],
        data: data,
        fill: false
        },
        
    ]
    },
    options: {
    responsive: true
    }
};

var ctx = document.getElementById('chart').getContext('2d');
window.myLine = new Chart(ctx, config);
};
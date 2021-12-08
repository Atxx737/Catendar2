var numTask= document.querySelector(".nu-task");
console.log("numTask",numTask.value);


var numTaskDone= document.querySelector(".nu-taskdone");
console.log("numTaskDone",numTaskDone.value);
    

var incomplete= numTask.value - numTaskDone.value;
console.log("incomplete",incomplete);
    
    
window.onload = function () {
var data = [numTaskDone.value,incomplete ];
var labels = ['Compelete','Incomplete' ];

var config = {
    type: 'doughnut',
    data: {
    labels: labels,
    datasets: [
        {
        label: 'Compelete',
        backgroundColor: [
        'rgba(74, 169, 108)',
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
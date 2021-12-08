var numTask= document.querySelector(".nu-task");
console.log("numTask",numTask);


var numTaskDone= document.querySelector(".nu-taskdone");

var incomplete= numTask.value- numTaskDone.value;
    
    
window.onload = function () {
var data = [numTaskDone.value,incomplete ];
var labels = ['Compelete','Incomple' ];

var config = {
    type: 'doughnut',
    data: {
    labels: labels,
    datasets: [
        {
        label: 'Incomple',
        backgroundColor: [
        '#D8E9A8',
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
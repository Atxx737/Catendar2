function percentTask(a, b,index){
    if ((a==0) && (b==0))
    {
        var c= 0;
    }
    else
    {
        var c= ((a/b)*100).toFixed(0);
    }
    
    var taskPercents= document.querySelectorAll(".task-percent");
    var progressBars= document.querySelectorAll(".progress-bar");
    progressBars[index].style.width=c+"%";
    taskPercents[index].innerText=c+'%';
      
    return c;
};


window.onload = function() {
    var numTasks= document.querySelectorAll(".nu-task");
    console.log("numTasks",numTasks);

    
    var numTaskDones= document.querySelectorAll(".nu-taskdone");
    
    numTasks.forEach(function(numTask,index){
        var numTaskDone= numTaskDones[index];
        
        console.log("percentTask",percentTask(numTaskDone.value,numTask.value,index));
    })
    

  };
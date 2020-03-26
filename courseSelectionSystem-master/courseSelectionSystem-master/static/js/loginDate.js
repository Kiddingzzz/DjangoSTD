var myChart=echarts.init(document.getElementById("lookdata"));
    var option={
        title:{
          text:'学生访问系统次数图'
        },
        toolbox:{
            show:true,
            feature:{
                saveAsImage:{
                    show:true
                }
            }
        },
        legend:{
            data:['时间']
        },
        xAxis:{
            data:["00:00-04:00","04:00-08:00","08:00-12:00","12:00-16:00","16:00-20:00","20:00-24:00"]
        },
        yAxis:{},
        series:[{
            name:'时间',
            type:'line',
            data:[40,20,35,60,55,10]
        }]
    };
    myChart.setOption(option);
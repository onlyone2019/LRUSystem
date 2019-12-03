/*******图一**********************************************/
var dom = document.getElementById("esspie");
var myesspie = echarts.init(dom);
var app = {};

option = null;
option = {
    title : {
        text: 'ESS属性分布',
        subtext: '空客A320neo',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: ['ESS=1','ESS=2','ESS=3']
    },
    series : [
        {
            name: 'ESS属性分布',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:[
                {value:657, name:'ESS=1'},
                {value:1002, name:'ESS=2'},
                {value:870, name:'ESS=3'},

            ],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};
if (option && typeof option === "object") {
    myesspie.setOption(option, true);
};
//开始分析ESS
function essAnaBt()
{
    var pselect =  $('#selectPmodel option:selected').val();
    //alert(pselect);
     $.ajax({
         type: "POST",
         url: '/getEss/',
         data: {"message": pselect},
         dataType: "text",
         success:function (json) {
             //alert(json);
             data_pie = JSON.parse(json);
             myesspie.setOption({
                 title : {
                      subtext: '机型' + pselect,
                 },
                    series: [{
                        data: data_pie,
                    }]
                });
         }
     });

}
/*******************************图二******************************************/
//供应商分析
var domMFRhis = document.getElementById("MFRhistogram");
var myMFRhis = echarts.init(domMFRhis);
var appMFR = {};
optionMFR = null;
optionMFR = {
    title : {
        text: 'LRU供应种类量前20的供应商代表图',
        subtext: 'A320'
    },
    tooltip : {
        trigger: 'axis'
    },
    toolbox: {
        show : true,
        feature : {
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    xAxis : [
        {
            type : 'category',
            data : ['624','0FF57','16827','3K723','4050G']
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'数量',
            type:'bar',
            label: {
                            normal: {
                                show: true,
                                position: 'top'
                            }
            },
            data:[81, 39,68, 32, 80],

        },

    ]
};
;
if (optionMFR && typeof optionMFR === "object") {
    myMFRhis.setOption(optionMFR, true);
}
//分析MFR
function mfrAnaBt(){
      var pselect =  $('#selectPmodelMFR option:selected').val();
    //alert(pselect);
     $.ajax({
         type: "POST",
         url: '/getMfrNumbers/',
         data: {"message": pselect},
         dataType: "text",
         success:function (json) {
             //alert(json);
             var data_his = JSON.parse(json);
             myMFRhis.setOption({
                 title : {
                      subtext: '机型' + pselect,
                 },
                 xAxis : [
                    {
                        type : 'category',
                        data : data_his['MFR'],
                    }
                ],
                 series: [{
                        name:'数量',
                        type:'bar',
                        label: {
                            normal: {
                                show: true,
                                position: 'top'
                            }
                        },
                        data:data_his['number'],
                    }]
                });
         }
     });

};
/*******************************图三******************************************/
//ATA章节分布分析
var domATA = document.getElementById("ATAhis");
var myATAhis = echarts.init(domATA);
var apphis = {};
optionATA = null;
var optionATA = {
   title: {
        text: 'LRU按照ATA章节的分布情况',
        subtext: 'A320'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
   toolbox: {
        show : true,
        feature : {
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true},
            dataZoom: {
 　　　　　　xAxisIndex:"none"
 　　　　　},
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'value',
        boundaryGap: [0, 0.01]
    },
    yAxis: {
        type: 'category',
        data: ['ATA77','ATA78','ATA76','ATA11']
    },
    series: [
        {
            name: '数量',
            type: 'bar',
            label: {
                            normal: {
                                show: true,
                                position: 'right'
                            }
                        },
            data: [24, 1, 1,83]
        },
    ]
};
;
if (optionATA && typeof optionATA === "object") {
    myATAhis.setOption(optionATA, true);
}


//分析ATA
function ataAnaBt(){
      var pselect =  $('#selectPmodelATA option:selected').val();
    //alert(pselect);
     $.ajax({
         type: "POST",
         url: '/getATANumbers/',
         data: {"message": pselect},
         dataType: "text",
         success:function (json) {
             //alert(json);
             var data_his = JSON.parse(json);
             myATAhis.setOption({
                 title : {
                      subtext: '机型' + pselect,
                 },
                 yAxis : [
                    {
                        type : 'category',
                        data : data_his['ATA'],
                    }
                ],
                 series: [{
                        name:'数量',
                        type:'bar',
                        label: {
                            normal: {
                                show: true,
                                position: 'right'
                            }
                        },
                        data:data_his['number'],
                    }]
                });
         }
     });

};
/*******************************图四******************************************/
//供应商分析
var domATAESS = document.getElementById("ATAESS");
var myATAESShis = echarts.init(domATAESS);
var appMFR = {};
optionATAESS = null;
optionATAESS = {
    title : {
        text: '部件按ATA章节的分布情况',
        subtext: '机型:A320,ESS:1'
    },
    tooltip : {
        trigger: 'axis'
    },
    toolbox: {
        show : true,
        feature : {
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    xAxis : [
        {
            type : 'category',
            data : ['624','0FF57','16827','3K723','4050G']
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'数量',
            type:'bar',
            label: {
                            normal: {
                                show: true,
                                position: 'top'
                            }
            },
            itemStyle:{
                normal:{
                    color:'#2f4554',
                }
            },
            data:[81, 39,68, 32, 80],

        },

    ]
};
;
if (optionATAESS && typeof optionATAESS === "object") {
    myATAESShis.setOption(optionATAESS, true);
}
//分析ESS不同部件分布
function ataessAnaBt(){
      var pselectPmode =  $('#selectPmodelATAESS option:selected').val();
      var pselectESS =  $('#selectESSThrid option:selected').val();
    //alert(pselect);
     $.ajax({
         type: "POST",
         url: '/getATAESSNumbers/',
         data: {"pmodel": pselectPmode,"ess":pselectESS},
         dataType: "text",
         success:function (json) {
             //alert(json);
             var data_his = JSON.parse(json);
             myATAESShis.setOption({
                 title : {
                      subtext: '机型:' + pselectPmode + ',ESS:' + pselectESS,
                 },
                 xAxis : [
                    {
                        type : 'category',
                        data : data_his['ATA'],
                    }
                ],
                 series: [{
                        name:'数量',
                        type:'bar',
                        label: {
                            normal: {
                                show: true,
                                position: 'top'
                            }
                        },
                        data:data_his['number'],
                    }]
                });
         }
     });

};

/*******图五**********************************************/
var domspc = document.getElementById("spcpie");
var myspcpie = echarts.init(domspc);
var appspc = {};

optionspc = null;
optionspc = {
    title : {
        text: 'SPC属性分布',
        subtext: '空客A320neo',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: ['SPC=1','SPC=2','SPC=6']
    },
    series : [
        {
            name: 'SPC属性分布',
            type:'pie',
            radius: ['40%', '60%'],
            avoidLabelOverlap: false,
            label: {
                normal: {
                    show: true,

                },
                emphasis: {
                    show: true,
                    textStyle: {
                        fontSize: '30',
                        fontWeight: 'bold'
                    }
                }
            },
            labelLine: {
                normal: {
                    show: true,
                }
            },

            data:[
                {value:1603, name:'SPC=1'},
                {value:21391, name:'SPC=2'},
                {value:6535, name:'SPC=6'},

            ],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};
if (optionspc && typeof optionspc === "object") {
    myspcpie.setOption(optionspc, true);
};
//开始分析spc
function spcAnaBt()
{
    var pselect =  $('#selectPmodelSPC option:selected').val();
    //alert(pselect);
     $.ajax({
         type: "POST",
         url: '/getSPC/',
         data: {"message": pselect},
         dataType: "text",
         success:function (json) {
             //alert(json);
             data_pie = JSON.parse(json);
             myspcpie.setOption({
                 title : {
                      subtext: '机型' + pselect,
                 },
                    series: [{
                        data: data_pie,
                    }]
                });
         }
     });

}
/*********图一*****************************/
var dom = document.getElementById("hisone");
var myChart = echarts.init(dom);
var app = {};
option = null;
option = {
    title : {
        text: '2018年底国内机队规模超过50架的航空公司',
        x:'center'
    },
    xAxis: {
        type: 'category',
        data: ['南方', '东方', '国际', '海南', '深圳', '厦门', '四川','山东','天津','上海','首都','春秋','吉祥','祥鹏'],
        axisLabel: {
                               interval: 0,
                               formatter:function(value)
                               {
                                   return value.split("").join("\n");
                               }
                           },
    },
    yAxis: {
        type: 'value'
    },

    series: [{
        data: [601,537,447,195,186,172,148,122,104,103,85,81,71,54],
         itemStyle:{
                                    normal:{
                                        color:'#4f81bd'
                                    }
                                },
         label: {
                            normal: {
                                show: true,
                                position: 'top'
                            }
            },
        type: 'bar'
    }]
};
;
if (option && typeof option === "object") {
    myChart.setOption(option, true);
}

/*********图二*****************************/
var dom2 = document.getElementById("histwo");
var myChart2 = echarts.init(dom2);
var app2 = {};
option2 = null;
option2 = {
    title : {
        text: '2018年底国内宽体机队机型统计情况',
        x:'center'
    },
    yAxis: {
          axisLabel: {
           show: true,
            textStyle: {
              fontSize : 8      //更改坐标轴文字大小
            }
        },
        type: 'category',
        data: ['B787-9', 'B787-8', 'B777-300/ER', 'B747-8', 'B747-400P', 'B350-900', 'A380','A330-300','A330-200']
    },
    xAxis: {
        type: 'value'
    },
    series: [{
        data: [57,29,58,7,3,13,5,131,106],
         label: {
                            normal: {
                                show: true,
                                position: 'right'
                            }
            },
        type: 'bar'
    }]
};
;
if (option2 && typeof option2 === "object") {
    myChart2.setOption(option2, true);
}


/*********图三****************************/
var dom3 = document.getElementById("histhree");
var myChart3 = echarts.init(dom3);
var app3 = {};
option3 = null;
option3 = {
    title : {
        text: '2018年底国内窄体机队机型统计情况',
        x:'center'
    },
    yAxis: {
        type: 'category',
         axisLabel: {
           show: true,
            textStyle: {
              fontSize : 8      //更改坐标轴文字大小
            }
        },
        data: ['B757-200', '737MAX8', 'B737-900/ER', 'B737-900', 'B737-800', 'B737-700', 'B737-300','A321neo','A321','A320neo','A320','A319']
    },
    xAxis: {
        type: 'value'
    },
    series: [{
        data: [4,86,6,5,1203,143,1,24,332,54,839,185],
        itemStyle:{
                                    normal:{
                                        color:'#4f81bd'
                                    }
                                },
         label: {
                            normal: {
                                show: true,
                                position: 'right'
                            }
            },
        type: 'bar'
    }]
};
;
if (option3 && typeof option3 === "object") {
    myChart3.setOption(option3, true);
}

/*********图四****************************/
var dom4 = document.getElementById("hisfour");
var myChart4 = echarts.init(dom4);
var app4 = {};
option4 = null;
option4 = {
     title : {
        text: '2018年底国内支线客机机队分布情况',
        x:'center'
    },
    legend: {
         orient: 'vertical',
        x:'right',
        y:'top',
        data: ['CR7','CRJ900','EMB145','EMB190','ARJ21-700','MA60']
    },
    tooltip: {},
    dataset: {
        source: [
            ['南方', , , , 20, ,],
            ['天津', , , 9, 52, , ],
            ['华夏', ,38, , , , ],
            ['成都', , , , , 1, ],
            ['河北', , , , 6, , ],
            ['幸福',, , , ,  25],
            ['北部湾', , , , 17, , ],
            ['乌鲁木齐', , , , 1, , ],
            ['多彩贵州', , , , 9, , ],
        ]
    },
    xAxis: {
         type: 'category',
         axisLabel: {
                               interval: 0,
                               formatter:function(value)
                               {
                                   return value.split("").join("\n");
                               }
                           },
    },
    yAxis: {},
    // Declare several bar series, each will be mapped
    // to a column of dataset.source by default.
    series: [
        {
            name: 'CR7',
            type: 'bar',
            label: {
                            normal: {
                                show: true,
                                position: 'top'
                            }
            },
        },
        {
            name: 'CRJ900',
            type: 'bar',
            label: {
                            normal: {
                                show: true,
                                position: 'top'
                            }
            },
        },
        {
            name: 'EMB145',
            type: 'bar',
            label: {
                            normal: {
                                show: true,
                                position: 'top'
                            }
            },
        },
        {
            name: 'EMB190',
            type: 'bar',
            label: {
                            normal: {
                                show:true,
                                position: 'top'
                            }
            },
        },
        {
            name: 'ARJ21-700',
            type: 'bar',
            label: {
                            normal: {
                                show:true,
                                position: 'top'
                            }
            },
        },
        {
            name: 'MA60',
            type: 'bar',
            label: {
                            normal: {
                                show:true,
                                position: 'top'
                            }
            },
        }
    ]
};
;
if (option4 && typeof option4 === "object") {
    myChart4.setOption(option4, true);
}
/*左侧导航栏ajax获取右侧表格*/
$(".getPnrsli").click(function(){
    /*alert( $(this).attr('id'));*/
    var selectId = $(this).attr('id');
   $.ajax({
                type:"post",
                url:"/getPnrs/",
                data:{"message":selectId},
                dataType:"text",
                success:function (data_json) {
                    var obj = JSON.parse(data_json);
                    /*alert(data_json);*/
                    /!*动态改变列*!/
                   $('#pnrListTable').datagrid({
                        columns:[[
                            {field:'mername',title:'制造商',width:100},
                            {field:'pmodel',title:'机型',width:60},
                            {field:'PNR',title:'PNR',width:80},
                            {field:'ATA',title:'ATA',width:80},
                            {field:'MFR',title:'MFR',width:80,align:'right'},
                            {field:'ADT',title:'ADT',width:80,align:'right'},
                            {field:'TPC',title:'TPC',width:100},
                            {field:'SPC',title:'SPC',width:60},
                            {field:'ESS',title:'ESS',width:80},
                            {field:'ATE',title:'ATE',width:80},
                            {field:'TCC',title:'TCC',width:80,align:'right'},
                            {field:'MTBUR',title:'MTBUR',width:80,align:'right'},
                            {field:'SCR',title:'SCR',width:100},
                            {field:'MST',title:'MST',width:60},
                            {field:'QPA',title:'QPA',width:80},
                            {field:'RFS',title:'RFS',width:80},
                            {field:'BFE',title:'BFE',width:80,align:'right'},
                            {field:'LTM',title:'LTM',width:80,align:'right'},
                            {field:'UNP',title:'UNP',width:100},
                            {field:'MSQ',title:'MSQ',width:60},
                            {field:'RPN',title:'RPN',width:80},
                            {field:'INC',title:'INC',width:80},
                            {field:'FUN',title:'FUN',width:80,align:'right'},
                            {field:'LRU Name',title:'LRU Name',width:80,align:'right'},
                            {field:'Access',title:'Access',width:100},
                            {field:'ZONE photos',title:'ZONE photos',width:60},
                            {field:'Dimension',title:'Dimension',width:60},
                            {field:'Body photos',title:'Body photos',width:80},
                            {field:'Man hours',title:'Man hours',width:80},
                            {field:'Mounting Type',title:'Mounting Type',width:80,align:'right'},
                            {field:'remov procedure',title:'remov procedure',width:80,align:'right'},
                            {field:'MTBR',title:'MTBR',width:100},
                            {field:'NHA 1',title:'NHA 1',width:60},
                            {field:'NHA 2',title:'NHA 2',width:60},
                            {field:'Cpclassname',title:'Cpclassname',width:60},
                        ]]
                    });

                   $('#pnrListTable').datagrid('loadData', obj);


                }
            })
});
/*高级查询控制按钮*/
function showAdvancePanel() {
    if ($("#advancePanel").css('display') == 'block')
        $("#advancePanel").css('display', 'none');
    else
    {
        $("#advancePanel").css('display', 'block');
        $.ajax({
            type: "POST",
            url: '/getATAs/',
            dataType: "json",
            success: function(json) {
                $('#advancelist').combobox({
                    data: "json.jsonResult.rows",
                    valueField: 'ID',
                    textField: 'TEXT'
                });
            }
        });

    }


}




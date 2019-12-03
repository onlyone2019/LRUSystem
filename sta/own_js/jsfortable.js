
/*生成菜单*/
function initSearchbox() {
        // $.parser.parse('#searchbox');
        // $.parser.parse('#mm');
        /// <summary>初始化下拉搜索框</summary>
            var m = $('#searchbox').searchbox('menu');
            if(m!=null)
            {
               /* m = null;
               if(m[0].hasChildNodes())
                {
                    var childs = m[0].children;
                    for(var i = childs .length - 1; i >= 0; i--) {
                      if(childs[i].class=="recl")
                            m[0].removeChild(childs[i]);
                    }
                }*/

            }
            else
            {
                addChildmenu();
                $('#searchbox').searchbox({
                menu: '#mm'
                });

                //将生成好的搜索框放入工具栏
                $(".datagrid-toolbar").append($("#searchboxWrapper"));
            }





}
function addChildmenu()
{
     var fields = null;
            fields = $('#pnrListTable').datagrid('getColumnFields');
            var father = document.getElementById("mm");
    for (var i = 0; i < fields.length; i++) {
                var divnodes = document.createElement("div");
                var opts = $('#pnrListTable').datagrid('getColumnOption', fields[i]);
                if (opts.table) {
                    //为div创建属性class = "recl"  
                    var divattr = document.createAttribute("class");  
                    divattr.value = "recl";        
                    //把属性class = "recl"添加到div  
                    divnodes.setAttributeNode(divattr);  
                    //为div创建属性names = "recl"  
                    var divattr2 = document.createAttribute("name");  
                    divattr2.value = opts.table + "." + opts.column;        
                    //把属性class = "recl"添加到div  
                    divnodes.setAttributeNode(divattr2);  

                    var text = document.createTextNode( opts.title );
                    divnodes.appendChild(text);
                    father.appendChild(divnodes);
                }
                else {
                    //为div创建属性class = "recl"  
                    var divattr = document.createAttribute("class");  
                    divattr.value = "recl";        
                    //把属性class = "recl"添加到div  
                    divnodes.setAttributeNode(divattr);  
                    //为div创建属性names = "recl"  
                    var divattr2 = document.createAttribute("name");  
                    divattr2.value =  fields[i];        
                    //把属性class = "recl"添加到div  
                    divnodes.setAttributeNode(divattr2);  

                    var text = document.createTextNode( opts.title);
                    divnodes.appendChild(text);
                    father.appendChild(divnodes);
                }
            };

}
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
                   $.parser.parse('#tb');
                   $('#pnrListTable').datagrid({

                        columns:[[
                           {field:'mername',title:'制造商',width:100,align:'center'},
                            {field:'pmodel',title:'机型',width:60,align:'center'},
                            {field:'PNR',title:'PNR',width:80,align:'center'},
                            {field:'ATA',title:'ATA',width:80,align:'center'},
                            {field:'MFR',title:'MFR',width:80,align:'center'},
                            {field:'ADT',title:'ADT',width:80,align:'center'},
                            {field:'TPC',title:'TPC',width:100,align:'center'},
                            {field:'SPC',title:'SPC',width:60,align:'center'},
                            {field:'ESS',title:'ESS',width:80,align:'center'},
                            {field:'ATE',title:'ATE',width:80,align:'center'},
                            {field:'TCC',title:'TCC',width:80,align:'center'},
                            {field:'MTBUR',title:'MTBUR',width:80,align:'center'},
                            {field:'SCR',title:'SCR',width:100,align:'center'},
                            {field:'MST',title:'MST',width:60,align:'center'},
                            {field:'QPA',title:'QPA',width:80,align:'center'},
                            {field:'RFS',title:'RFS',width:80,align:'center'},
                            {field:'BFE',title:'BFE',width:80,align:'center'},
                            {field:'LTM',title:'LTM',width:80,align:'center'},
                            {field:'UNP',title:'UNP',width:100,align:'center'},
                            {field:'MSQ',title:'MSQ',width:60,align:'center'},
                            {field:'RPN',title:'RPN',width:80,align:'center'},
                            {field:'INC',title:'INC',width:80,align:'center'},
                            {field:'FUN',title:'FUN',width:80,align:'center'},
                            {field:'LRU Name',title:'LRU Name',width:80,align:'center'},
                            {field:'Access',title:'Access',width:100,align:'center'},
                            {field:'ZONE photos',title:'ZONE photos',width:60,align:'center'},
                            {field:'Dimension',title:'Dimension',width:60,align:'center'},
                            {field:'Body photos',title:'Body photos',width:80,align:'center'},
                            {field:'Man hours',title:'Man hours',width:80,align:'center'},
                            {field:'Mounting Type',title:'Mounting Type',width:80,align:'center'},
                            {field:'remov procedure',title:'remov procedure',width:80,align:'center'},
                            {field:'MTBR',title:'MTBR',width:100,align:'center'},
                            {field:'NHA 1',title:'NHA 1',width:60,align:'center'},
                            {field:'NHA 2',title:'NHA 2',width:60,align:'center'},
                            {field:'Cpclassname',title:'Cpclassname',width:60,align:'center'},
                        ]]
                    });

                   $('#pnrListTable').datagrid('loadData', obj);
                   initSearchbox();

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
            url: '/getManuPmodelATAs/',
            dataType: "text",
            success: function(json_str) {
                all_data = JSON.parse(json_str)
                $('#atalist').combobox({
                    data: all_data['ATA'],
                    valueField: 'id',
                    textField: 'text'
                });
                $('#manufacturelist').combobox({
                    data: all_data['Mername'],
                    valueField: 'id',
                    textField: 'text'
                });
                $('#pmodellist').combobox({
                    data: all_data['PModelname'],
                    valueField: 'id',
                    textField: 'text'
                });
            }
        });


    }


}
/*高级查询按钮*/
function advSearch(){
    var ATAs = $('#atalist').combobox('getValues').toString();
    var Manus = $('#manufacturelist').combobox('getValues').toString();
    var Pmodel = $('#pmodellist').combobox('getValues').toString();
    var json_data = {};
/*    json_data['ATAs'] = ATAs;
    json_data['PModelnames'] = Pmodel;
    json_data['Mernames'] = Manus;
    send_str = JSON.stringify(json_data);
    alert(send_str);*/
    $.ajax({
         type: "POST",
         url: '/getAdvancePnrs/',
         data:{"ATAs":ATAs,"PModelnames":Pmodel,"Mernames":Manus},
         dataType: "text",
        success:function (json_str) {
            /* alert(json_str)*/
            var obj = JSON.parse(json_str);
                    /*alert(data_json);*/
                    /*动态解析渲染图标*/
                    $.parser.parse('#tb');
                    /!*动态改变列*!/
                   $('#pnrListTable').datagrid({
                        columns:[[
                           {field:'mername',title:'制造商',width:100,align:'center'},
                            {field:'pmodel',title:'机型',width:60,align:'center'},
                            {field:'PNR',title:'PNR',width:80,align:'center'},
                            {field:'ATA',title:'ATA',width:80,align:'center'},
                            {field:'MFR',title:'MFR',width:80,align:'center'},
                            {field:'ADT',title:'ADT',width:80,align:'center'},
                            {field:'TPC',title:'TPC',width:100,align:'center'},
                            {field:'SPC',title:'SPC',width:60,align:'center'},
                            {field:'ESS',title:'ESS',width:80,align:'center'},
                            {field:'ATE',title:'ATE',width:80,align:'center'},
                            {field:'TCC',title:'TCC',width:80,align:'center'},
                            {field:'MTBUR',title:'MTBUR',width:80,align:'center'},
                            {field:'SCR',title:'SCR',width:100,align:'center'},
                            {field:'MST',title:'MST',width:60,align:'center'},
                            {field:'QPA',title:'QPA',width:80,align:'center'},
                            {field:'RFS',title:'RFS',width:80,align:'center'},
                            {field:'BFE',title:'BFE',width:80,align:'center'},
                            {field:'LTM',title:'LTM',width:80,align:'center'},
                            {field:'UNP',title:'UNP',width:100,align:'center'},
                            {field:'MSQ',title:'MSQ',width:60,align:'center'},
                            {field:'RPN',title:'RPN',width:80,align:'center'},
                            {field:'INC',title:'INC',width:80,align:'center'},
                            {field:'FUN',title:'FUN',width:80,align:'center'},
                            {field:'LRU Name',title:'LRU Name',width:80,align:'center'},
                            {field:'Access',title:'Access',width:100,align:'center'},
                            {field:'ZONE photos',title:'ZONE photos',width:60,align:'center'},
                            {field:'Dimension',title:'Dimension',width:60,align:'center'},
                            {field:'Body photos',title:'Body photos',width:80,align:'center'},
                            {field:'Man hours',title:'Man hours',width:80,align:'center'},
                            {field:'Mounting Type',title:'Mounting Type',width:80,align:'center'},
                            {field:'remov procedure',title:'remov procedure',width:80,align:'center'},
                            {field:'MTBR',title:'MTBR',width:100,align:'center'},
                            {field:'NHA 1',title:'NHA 1',width:60,align:'center'},
                            {field:'NHA 2',title:'NHA 2',width:60,align:'center'},
                            {field:'Cpclassname',title:'Cpclassname',width:60,align:'center'},
                        ]]
                    });

                   $('#pnrListTable').datagrid('loadData', obj);
                   initSearchbox();

        }
    });
}

/*高级查询按钮*/
function allSearch(){
    $.ajax({
         type: "POST",
         url: '/getAllPnrs/',
         dataType: "text",
        success:function (json_str) {
            /* alert(json_str)*/
            var obj = JSON.parse(json_str);
                    /*alert(data_json);*/
                    $.parser.parse('#tb');
                    /!*动态改变列*!/
                   $('#pnrListTable').datagrid({
                        columns:[[
                            {field:'mername',title:'制造商',width:100,align:'center'},
                            {field:'pmodel',title:'机型',width:60,align:'center'},
                            {field:'PNR',title:'PNR',width:80,align:'center'},
                            {field:'ATA',title:'ATA',width:80,align:'center'},
                            {field:'MFR',title:'MFR',width:80,align:'center'},
                            {field:'ADT',title:'ADT',width:80,align:'center'},
                            {field:'TPC',title:'TPC',width:100,align:'center'},
                            {field:'SPC',title:'SPC',width:60,align:'center'},
                            {field:'ESS',title:'ESS',width:80,align:'center'},
                            {field:'ATE',title:'ATE',width:80,align:'center'},
                            {field:'TCC',title:'TCC',width:80,align:'center'},
                            {field:'MTBUR',title:'MTBUR',width:80,align:'center'},
                            {field:'SCR',title:'SCR',width:100,align:'center'},
                            {field:'MST',title:'MST',width:60,align:'center'},
                            {field:'QPA',title:'QPA',width:80,align:'center'},
                            {field:'RFS',title:'RFS',width:80,align:'center'},
                            {field:'BFE',title:'BFE',width:80,align:'center'},
                            {field:'LTM',title:'LTM',width:80,align:'center'},
                            {field:'UNP',title:'UNP',width:100,align:'center'},
                            {field:'MSQ',title:'MSQ',width:60,align:'center'},
                            {field:'RPN',title:'RPN',width:80,align:'center'},
                            {field:'INC',title:'INC',width:80,align:'center'},
                            {field:'FUN',title:'FUN',width:80,align:'center'},
                            {field:'LRU Name',title:'LRU Name',width:80,align:'center'},
                            {field:'Access',title:'Access',width:100,align:'center'},
                            {field:'ZONE photos',title:'ZONE photos',width:60,align:'center'},
                            {field:'Dimension',title:'Dimension',width:60,align:'center'},
                            {field:'Body photos',title:'Body photos',width:80,align:'center'},
                            {field:'Man hours',title:'Man hours',width:80,align:'center'},
                            {field:'Mounting Type',title:'Mounting Type',width:80,align:'center'},
                            {field:'remov procedure',title:'remov procedure',width:80,align:'center'},
                            {field:'MTBR',title:'MTBR',width:100,align:'center'},
                            {field:'NHA 1',title:'NHA 1',width:60,align:'center'},
                            {field:'NHA 2',title:'NHA 2',width:60,align:'center'},
                            {field:'Cpclassname',title:'Cpclassname',width:60,align:'center'},
                        ]]
                    });

                   $('#pnrListTable').datagrid('loadData', obj);
                   initSearchbox();

        }
    });
}


/*属性筛选按钮*/
function showPropertyPanel() {
    if ($("#propertyPanel").css('display') == 'block')
        $("#propertyPanel").css('display', 'none');
    else
    {
        $("#propertyPanel").css('display', 'block');
        $.ajax({
            type: "POST",
            url: '/getPropertysaAndClass/',
            dataType: "text",
            success: function(json_str) {
                all_data = JSON.parse(json_str)
                $('#propertylist').combobox({
                    data: all_data['CPnameList'],
                    valueField: 'id',
                    textField: 'text'
                });
                $('#classlist').combobox({
                    data: all_data['ClanameList'],
                    valueField: 'id',
                    textField: 'text'
                });

            }
        });


    }
}
/*筛选属性*/
function propertySelect()
{
    var datanumber = 0;
    var all_protery;
    try {
        datanumber = $("#pnrListTable").datagrid("getData").total;
        all_protery  = $('#pnrListTable').datagrid('getColumnFields');
    }
    catch(err){
        alert("请先选择数据");
        return;
    }

    if(0 == datanumber)
    {
        alert("请先选择数据");
        return;
    }
    var propertySelect = $('#propertylist').combobox('getValues').toString();
    if (isEmpty(propertySelect))
    {
        alert("请选择筛选属性");
        return;
    }
    var filedIDs = propertySelect.split(",");
    //无法隐藏属性
    filedIDs.push('mername')
    filedIDs.push('pmodel')
    filedIDs.push('PNR')
    var res = cj(all_protery,filedIDs)
    //alert(res)

    for (var i = 0;i < all_protery.length;i++)
    {
        $('#pnrListTable').datagrid('showColumn', all_protery[i]);
    }
    for (var i = 0;i < res.length;i++)
    {
        $('#pnrListTable').datagrid('hideColumn', res[i]);
    }


}
/*分级筛选属性*/
function classSelect()
{
    var datanumber = 0;
    var all_protery;
    try {
        datanumber = $("#pnrListTable").datagrid("getData").total;
        all_protery  = $('#pnrListTable').datagrid('getColumnFields');
    }
    catch(err){
        alert("请先选择数据");
        return;
    }

    if(0 == datanumber)
    {
        alert("请先选择数据");
        return;
    }
    var classSelect = $('#classlist').combobox('getValues').toString();
    if (isEmpty(classSelect))
    {
        alert("请选择分级名称");
        return;
    }
    /*获取分级属性名*/
    $.ajax({
            type: "POST",
            data:{"message" : classSelect},
            url: '/getClassPropertys/',
            dataType: "text",
            success: function(json_str) {
                all_data = JSON.parse(json_str)
                //无法隐藏属性
                var res = cj(all_protery,all_data)
                //alert(res)

                for (var i = 0;i < all_protery.length;i++)
                {
                    $('#pnrListTable').datagrid('showColumn', all_protery[i]);
                }
                for (var i = 0;i < res.length;i++)
                {
                    $('#pnrListTable').datagrid('hideColumn', res[i]);
                }

            }
        });


}
/*查看全部属性数据*/
function propertyAllSelect()
{
    var datanumber = 0;
    var all_protery;
    try {
        datanumber = $("#pnrListTable").datagrid("getData").total;
        all_protery  = $('#pnrListTable').datagrid('getColumnFields');
    }
    catch(err){
        alert("请先选择数据");
        return;
    }

    if(0 == datanumber)
    {
        alert("请先选择数据");
        return;
    }
    for (var i = 0;i < all_protery.length;i++)
    {
        $('#pnrListTable').datagrid('showColumn', all_protery[i]);
    }

}

/*工具栏搜索按钮*/
function toolBarSearcher(value, name) {
            /// <summary>搜索列表</summary>
    //alert('value:'+value+' name:'+name);
    var datas;
    try {
        //datas = $('#pnrListTable').datagrid('getRows');
        datas = $("#pnrListTable").datagrid("getData");
    }
    catch(err){
        alert("数据源出错");
        return;
    }
    var datanumber = datas.total;
    if(0 == datanumber)
    {
        alert("没有数据");
        return;
    }
    if(isEmpty(value))
    {
        alert("请输入搜索内容");
        return;
    }
    var rows = [];
    $('#pnrListTable').datagrid('unselectAll');
    for (var i = 0;i < datanumber;i++)
    {
        if(value == datas.rows[i][name.toString()])
        {
            rows.push(i)
            $('#pnrListTable').datagrid('selectRow',i);
        }
    }
    if(0 == rows.length)
    {
        alert("当前查询数据没有搜索结果...");
    }


}
/*点击按钮显示属性*/
function dialogPropData() {
    $.ajax({
        type: "POST",
        url: '/getAllPropertyInfos/',
        dataType: "text",
        success:function (json_str) {
            $.parser.parse('#dialogProper');
            $.parser.parse('#tbproty');
            var obj = JSON.parse(json_str);
                //alert(json_str);
             $('#propretyListTable').datagrid({
                        columns:[[
                            {field:'CPname',title:'属性名',width:100,align:'center'},
                            {field:'CPremark',title:'解释',width:300,align:'center'},
                            {field:'CPother',title:'备注',width:100,align:'center'},
                        ]]
                    });
             $('#propretyListTable').datagrid('loadData', obj);
             $('#dd').dialog({
                         modal: true
                    });

              /*$('#propretyListTable').datagrid("options").view.onAfterRender = function (target, rows) {
              $('#dd').dialog({
                         modal: true
                    });
                  //$('#dialogProper').modal('show');
                };*/



             //setTimeout(function(){ $('#dialogProper').modal('show'); }, 3000);

        }

    });

}


/*
判断字符串为空
 */
function isEmpty(obj){
    if(typeof obj == "undefined" || obj == null || obj == ""){
        return true;
    }else{
        return false;
    }
}
/*求集合差集*/
function cj(a,b){
				//因为splice()方法会改变原始数组，所以使用slice()方法克隆数组，保证原始数组不被改变，方便多次运算
				var aa=a.slice();
				var bb=b.slice();
				for(x in bb){
					var y=aa.indexOf(bb[x]);
					if(y>=0){
						aa.splice(y,1);
					}
				}
				return aa;
}



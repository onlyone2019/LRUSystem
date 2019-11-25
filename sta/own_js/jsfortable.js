
	var setting = {
		treeObj : null,
		check: {
			enable: true
		},
		data: {
			simpleData: {
				enable: true,
				idKey: "id",
				pIdKey: "pId",
				rootPId: 0
			}
		},
		callback: {
			onCheck: zTreeOnCheck
		},
		view: {
			showLine: false,
			showIcon: false,
			showTitle: false,
			// fontCss : {color:"red"}
		}
		
	};

	var zNodes =[{"id":"1","pId":"0","securityOptions":[],"corpCode":"","PERMITID":"","name":"临时设施","PROJECTNAME":"","corpId":""},{"id":"11","pId":"1","securityOptions":[],"corpCode":"","PERMITID":"","name":"施工区","PROJECTNAME":"","corpId":""},{"id":"111","pId":"11","securityOptions":[],"corpCode":"","PERMITID":"","name":"门卫室","PROJECTNAME":"","corpId":""},{"id":"112","pId":"11","securityOptions":[],"corpCode":"","PERMITID":"","name":"配电室","PROJECTNAME":"","corpId":""},{"id":"113","pId":"11","securityOptions":[],"corpCode":"","PERMITID":"","name":"仓库","PROJECTNAME":"","corpId":""},{"id":"114","pId":"11","securityOptions":[],"corpCode":"","PERMITID":"","name":"卷场机操作室","PROJECTNAME":"","corpId":""},{"id":"115","pId":"11","securityOptions":[],"corpCode":"","PERMITID":"","name":"饮水室、吸烟室","PROJECTNAME":"","corpId":""},{"id":"12","pId":"1","securityOptions":[],"corpCode":"","PERMITID":"","name":"办公区","PROJECTNAME":"","corpId":""},{"id":"121","pId":"12","securityOptions":[],"corpCode":"","PERMITID":"","name":"办公室","PROJECTNAME":"","corpId":""},{"id":"122","pId":"12","securityOptions":[],"corpCode":"","PERMITID":"","name":"医务保健室","PROJECTNAME":"","corpId":""},{"id":"123","pId":"12","securityOptions":[],"corpCode":"","PERMITID":"","name":"会议室","PROJECTNAME":"","corpId":""},{"id":"124","pId":"12","securityOptions":[],"corpCode":"","PERMITID":"","name":"现场监控","PROJECTNAME":"","corpId":""},{"id":"13","pId":"1","securityOptions":[],"corpCode":"","PERMITID":"","name":"生活区","PROJECTNAME":"","corpId":""},{"id":"131","pId":"13","securityOptions":[],"corpCode":"","PERMITID":"","name":"宿舍","PROJECTNAME":"","corpId":""},{"id":"132","pId":"13","securityOptions":[],"corpCode":"","PERMITID":"","name":"食堂和储物间","PROJECTNAME":"","corpId":""},{"id":"133","pId":"13","securityOptions":[],"corpCode":"","PERMITID":"","name":"活动室","PROJECTNAME":"","corpId":""},{"id":"134","pId":"13","securityOptions":[],"corpCode":"","PERMITID":"","name":"卫生间","PROJECTNAME":"","corpId":""},{"id":"135","pId":"13","securityOptions":[],"corpCode":"","PERMITID":"","name":"淋浴间","PROJECTNAME":"","corpId":""},{"id":"136","pId":"13","securityOptions":[],"corpCode":"","PERMITID":"","name":"洗漱间","PROJECTNAME":"","corpId":""},{"id":"2","pId":"0","securityOptions":[],"corpCode":"","PERMITID":"","name":"安全防护","PROJECTNAME":"","corpId":""},{"id":"21","pId":"2","securityOptions":[],"corpCode":"","PERMITID":"","name":"防护棚","PROJECTNAME":"","corpId":""},{"id":"211","pId":"21","securityOptions":[],"corpCode":"","PERMITID":"","name":"钢筋、木工作业区防护棚","PROJECTNAME":"","corpId":""},{"id":"212","pId":"21","securityOptions":[],"corpCode":"","PERMITID":"","name":"搅拌设备防护棚","PROJECTNAME":"","corpId":""},{"id":"22","pId":"2","securityOptions":[],"corpCode":"","PERMITID":"","name":"临边防护","PROJECTNAME":"","corpId":""},{"id":"221","pId":"22","securityOptions":[],"corpCode":"","PERMITID":"","name":"基坑周边防护","PROJECTNAME":"","corpId":""},{"id":"222","pId":"22","securityOptions":[],"corpCode":"","PERMITID":"","name":"楼层、阳台临边防护","PROJECTNAME":"","corpId":""},{"id":"223","pId":"22","securityOptions":[],"corpCode":"","PERMITID":"","name":"楼梯临边防护","PROJECTNAME":"","corpId":""},{"id":"224","pId":"22","securityOptions":[],"corpCode":"","PERMITID":"","name":"竖向洞口防护","PROJECTNAME":"","corpId":""},{"id":"225","pId":"22","securityOptions":[],"corpCode":"","PERMITID":"","name":"屋面临边防护","PROJECTNAME":"","corpId":""},{"id":"226","pId":"22","securityOptions":[],"corpCode":"","PERMITID":"","name":"安全通道","PROJECTNAME":"","corpId":""},{"id":"227","pId":"22","securityOptions":[],"corpCode":"","PERMITID":"","name":"电梯门、进口防护","PROJECTNAME":"","corpId":""},{"id":"228","pId":"22","securityOptions":[],"corpCode":"","PERMITID":"","name":"水平预留洞口防护","PROJECTNAME":"","corpId":""},{"id":"229","pId":"22","securityOptions":[],"corpCode":"","PERMITID":"","name":"悬挑式钢平台","PROJECTNAME":"","corpId":""},{"id":"3","pId":"0","securityOptions":[],"corpCode":"","PERMITID":"","name":"消防设施","PROJECTNAME":"","corpId":""},{"id":"4","pId":"0","securityOptions":[],"corpCode":"","PERMITID":"","name":"临时用电","PROJECTNAME":"","corpId":""},{"id":"41","pId":"4","securityOptions":[],"corpCode":"","PERMITID":"","name":"总配电柜(箱)、分配电箱、开关箱安装设置","PROJECTNAME":"","corpId":""},{"id":"411","pId":"41","securityOptions":[],"corpCode":"","PERMITID":"","name":"总配电柜(箱)","PROJECTNAME":"","corpId":""},{"id":"412","pId":"41","securityOptions":[],"corpCode":"","PERMITID":"","name":"分配电箱","PROJECTNAME":"","corpId":""},{"id":"413","pId":"41","securityOptions":[],"corpCode":"","PERMITID":"","name":"开关箱","PROJECTNAME":"","corpId":""},{"id":"5","pId":"0","securityOptions":[],"corpCode":"","PERMITID":"","name":"脚手架","PROJECTNAME":"","corpId":""},{"id":"51","pId":"5","securityOptions":[],"corpCode":"","PERMITID":"","name":"扣件式钢管脚手架","PROJECTNAME":"","corpId":""},{"id":"52","pId":"5","securityOptions":[],"corpCode":"","PERMITID":"","name":"型钢悬挑式脚手架","PROJECTNAME":"","corpId":""},{"id":"53","pId":"5","securityOptions":[],"corpCode":"","PERMITID":"","name":"满堂脚手架","PROJECTNAME":"","corpId":""},{"id":"54","pId":"5","securityOptions":[],"corpCode":"","PERMITID":"","name":"满堂支撑架","PROJECTNAME":"","corpId":""},{"id":"6","pId":"0","securityOptions":[],"corpCode":"","PERMITID":"","name":"基坑支护","PROJECTNAME":"","corpId":""},{"id":"61","pId":"6","securityOptions":[],"corpCode":"","PERMITID":"","name":"型钢桩横挡板支护","PROJECTNAME":"","corpId":""},{"id":"62","pId":"6","securityOptions":[],"corpCode":"","PERMITID":"","name":"混凝土灌注桩支护","PROJECTNAME":"","corpId":""},{"id":"63","pId":"6","securityOptions":[],"corpCode":"","PERMITID":"","name":"土钉墙支护","PROJECTNAME":"","corpId":""},{"id":"7","pId":"0","securityOptions":[],"corpCode":"","PERMITID":"","name":"起重机械设备","PROJECTNAME":"","corpId":""},{"id":"71","pId":"7","securityOptions":[],"corpCode":"","PERMITID":"","name":"塔吊","PROJECTNAME":"","corpId":""},{"id":"711","pId":"71","securityOptions":[],"corpCode":"","PERMITID":"","name":"保险装置设置和有效性","PROJECTNAME":"","corpId":""},{"id":"712","pId":"71","securityOptions":[],"corpCode":"","PERMITID":"","name":"多塔作业防碰撞措施","PROJECTNAME":"","corpId":""},{"id":"713","pId":"71","securityOptions":[],"corpCode":"","PERMITID":"","name":"基础安全状况","PROJECTNAME":"","corpId":""},{"id":"714","pId":"71","securityOptions":[],"corpCode":"","PERMITID":"","name":"与外电线路安全距离","PROJECTNAME":"","corpId":""},{"id":"715","pId":"71","securityOptions":[],"corpCode":"","PERMITID":"","name":"基础防护","PROJECTNAME":"","corpId":""},{"id":"716","pId":"71","securityOptions":[],"corpCode":"","PERMITID":"","name":"附着安全状况","PROJECTNAME":"","corpId":""},{"id":"717","pId":"71","securityOptions":[],"corpCode":"","PERMITID":"","name":"《黑龙江省建筑起重机械设备使用登记证》","PROJECTNAME":"","corpId":""},{"id":"72","pId":"7","securityOptions":[],"corpCode":"","PERMITID":"","name":"施工升降机","PROJECTNAME":"","corpId":""},{"id":"721","pId":"72","securityOptions":[],"corpCode":"","PERMITID":"","name":"防坠落安全器有效标定期情况","PROJECTNAME":"","corpId":""},{"id":"722","pId":"72","securityOptions":[],"corpCode":"","PERMITID":"","name":"保险装置设置和有效性","PROJECTNAME":"","corpId":""},{"id":"723","pId":"72","securityOptions":[],"corpCode":"","PERMITID":"","name":"基础安全状况","PROJECTNAME":"","corpId":""},{"id":"724","pId":"72","securityOptions":[],"corpCode":"","PERMITID":"","name":"进出主体通道防护架体安全状况","PROJECTNAME":"","corpId":""},{"id":"725","pId":"72","securityOptions":[],"corpCode":"","PERMITID":"","name":"楼层设置层数标志牌、安全标示牌","PROJECTNAME":"","corpId":""},{"id":"726","pId":"72","securityOptions":[],"corpCode":"","PERMITID":"","name":"平台出入口处安装金属防护门","PROJECTNAME":"","corpId":""},{"id":"727","pId":"72","securityOptions":[],"corpCode":"","PERMITID":"","name":"平台两侧设置防护栏杆封闭","PROJECTNAME":"","corpId":""},{"id":"728","pId":"72","securityOptions":[],"corpCode":"","PERMITID":"","name":"《黑龙江省建筑起重机械设备使用登记证》","PROJECTNAME":"","corpId":""},{"id":"73","pId":"7","securityOptions":[],"corpCode":"","PERMITID":"","name":"物料提升机","PROJECTNAME":"","corpId":""},{"id":"731","pId":"73","securityOptions":[],"corpCode":"","PERMITID":"","name":"保险装置设置和有效性","PROJECTNAME":"","corpId":""},{"id":"732","pId":"73","securityOptions":[],"corpCode":"","PERMITID":"","name":"平台出入口处安装金属防护门","PROJECTNAME":"","corpId":""},{"id":"733","pId":"73","securityOptions":[],"corpCode":"","PERMITID":"","name":"平台两侧设置防护栏杆封闭","PROJECTNAME":"","corpId":""},{"id":"734","pId":"73","securityOptions":[],"corpCode":"","PERMITID":"","name":"进出主体通道防护架体安装状况","PROJECTNAME":"","corpId":""},{"id":"735","pId":"73","securityOptions":[],"corpCode":"","PERMITID":"","name":"楼层设置层数标志牌、安全标示牌","PROJECTNAME":"","corpId":""},{"id":"736","pId":"73","securityOptions":[],"corpCode":"","PERMITID":"","name":"龙门架设置缆风绳安全状况","PROJECTNAME":"","corpId":""},{"id":"737","pId":"73","securityOptions":[],"corpCode":"","PERMITID":"","name":"卷扬机防护棚防砸、防雨状况","PROJECTNAME":"","corpId":""},{"id":"738","pId":"73","securityOptions":[],"corpCode":"","PERMITID":"","name":"基础安全状况","PROJECTNAME":"","corpId":""},{"id":"739","pId":"73","securityOptions":[],"corpCode":"","PERMITID":"","name":"《黑龙江省建筑起重机械设备使用登记证》","PROJECTNAME":"","corpId":""},{"id":"8","pId":"0","securityOptions":[],"corpCode":"","PERMITID":"","name":"文明施工","PROJECTNAME":"","corpId":""},{"id":"81","pId":"8","securityOptions":[],"corpCode":"","PERMITID":"","name":"封闭施工","PROJECTNAME":"","corpId":""},{"id":"811","pId":"81","securityOptions":[],"corpCode":"","PERMITID":"","name":"大门","PROJECTNAME":"","corpId":""},{"id":"812","pId":"81","securityOptions":[],"corpCode":"","PERMITID":"","name":"现场围挡","PROJECTNAME":"","corpId":""},{"id":"82","pId":"8","securityOptions":[],"corpCode":"","PERMITID":"","name":"施工场地","PROJECTNAME":"","corpId":""},{"id":"821","pId":"82","securityOptions":[],"corpCode":"","PERMITID":"","name":"施工现场主要干道、场地硬化","PROJECTNAME":"","corpId":""},{"id":"822","pId":"82","securityOptions":[],"corpCode":"","PERMITID":"","name":"裸土绿化和覆盖","PROJECTNAME":"","corpId":""},{"id":"823","pId":"82","securityOptions":[],"corpCode":"","PERMITID":"","name":"施工现场扬尘监测设备、洒水车、吸尘车、移动雾炮车和喷淋装置等防尘设备设置","PROJECTNAME":"","corpId":""},{"id":"824","pId":"82","securityOptions":[],"corpCode":"","PERMITID":"","name":"出口设置车辆清洗设备设置","PROJECTNAME":"","corpId":""},{"id":"83","pId":"8","securityOptions":[],"corpCode":"","PERMITID":"","name":"安全标志","PROJECTNAME":"","corpId":""},{"id":"831","pId":"83","securityOptions":[],"corpCode":"","PERMITID":"","name":"安全旗","PROJECTNAME":"","corpId":""},{"id":"832","pId":"83","securityOptions":[],"corpCode":"","PERMITID":"","name":"“五牌一图”","PROJECTNAME":"","corpId":""},{"id":"833","pId":"83","securityOptions":[],"corpCode":"","PERMITID":"","name":"工作着装、公示栏、形象镜","PROJECTNAME":"","corpId":""},{"id":"834","pId":"83","securityOptions":[],"corpCode":"","PERMITID":"","name":"安全挂图","PROJECTNAME":"","corpId":""},{"id":"835","pId":"83","securityOptions":[],"corpCode":"","PERMITID":"","name":"安全警示标牌","PROJECTNAME":"","corpId":""},{"id":"84","pId":"8","securityOptions":[],"corpCode":"","PERMITID":"","name":"隔离围挡与材料堆放","PROJECTNAME":"","corpId":""},{"id":"841","pId":"84","securityOptions":[],"corpCode":"","PERMITID":"","name":"作业区围挡","PROJECTNAME":"","corpId":""},{"id":"842","pId":"84","securityOptions":[],"corpCode":"","PERMITID":"","name":"材料堆放","PROJECTNAME":"","corpId":""},{"id":"85","pId":"8","securityOptions":[],"corpCode":"","PERMITID":"","name":"标识牌","PROJECTNAME":"","corpId":""},{"id":"851","pId":"85","securityOptions":[],"corpCode":"","PERMITID":"","name":"材料标识牌","PROJECTNAME":"","corpId":""},{"id":"852","pId":"85","securityOptions":[],"corpCode":"","PERMITID":"","name":"手脚架验收合格牌","PROJECTNAME":"","corpId":""},{"id":"853","pId":"85","securityOptions":[],"corpCode":"","PERMITID":"","name":"机械负责人标识牌","PROJECTNAME":"","corpId":""},{"id":"854","pId":"85","securityOptions":[],"corpCode":"","PERMITID":"","name":"限重标识牌","PROJECTNAME":"","corpId":""},{"id":"0","pId":"","securityOptions":[],"corpCode":"","PERMITID":"","name":"棚户区改造配套基础设施建设项目","PROJECTNAME":"","corpId":""}]
	
	var code;
	
	function setCheck() {
		var zTree = $.fn.zTree.getZTreeObj("treeDemo"),
			type = {Y: "ps", N: "ps"}
		zTree.setting.check.chkboxType = type;
		zTree.expandAll(true); //全部展开
		showCode('setting.check.chkboxType = { "Y" : "' + type.Y + '", "N" : "' + type.N + '" };');
		minejs();
	}
	function showCode(str) {
		if (!code) code = $("#code");
		code.empty();
		code.append("<li>"+str+"</li>");
	}

	function zTreeOnCheck(event, treeId, treeNode) {
		getSelectedNodes();
		//当前被选中对象携带参数
		// console.log(treeNode.tId + ", " + treeNode.name + "," + treeNode.checked);
	};
	

	function getSelectedNodes(){
		// var zTree = $.fn.zTree.getZTreeObj("treeDemo");
		// var selectedNode = zTree.getCheckedNodes();

		// 获取当前被勾选的节点集合
		var treeObj = $.fn.zTree.getZTreeObj("treeDemo");
		var nodes = treeObj.getCheckedNodes(true);
	}

	$(document).ready(function(){
		$.fn.zTree.init($("#treeDemo"), setting, zNodes);
		setCheck();
		$("#py").bind("change", setCheck);
		$("#sy").bind("change", setCheck);
		$("#pn").bind("change", setCheck);
		$("#sn").bind("change", setCheck);
		$('.ztree li span.button.switch').click(function(){
			minejs();
		})
	});
	function minejs(){
		
	}
#encoding=utf-8
from bs4 import BeautifulSoup
import re
html_str='''
<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>杭州租房网_杭州合租|房屋出租信息网_青客时尚租房网</title>
<meta http-equiv="Cache-Control" content="no-transform " />
<meta name="applicable-device" content="pc">
<meta name="keywords"
	 content="杭州租房网、杭州合租、杭州房屋出租、杭州租房信息网"   />
<meta name="description"
	 content="青客租房网提供杭州同城全新全面的房屋出租信息，所有租房统一装修、设施齐全、租房临近地铁、无中介、定期保洁，是居家生活办公首选。杭州租房、找合租、个人房屋出租，就上青客租房网。"   />
<link rel="alternate" media="only screen and (max-width: 640px)"
	
			href="https://i.qk365.com/hz/list/"
		
		/>
<link href="https://hz.qk365.com/css/find.css?version=20180717" rel="stylesheet" type="text/css">
<script type="text/javascript" src="https://hz.qk365.com/js/homepage/defaultPic.js"></script>
<style type="text/css">
	.jg_pic {
		width: 1170px;
		height: 160px;
		margin: 20px auto;
	}
	.jg_pic img {
		width: 1170px;
		height: 160px;
	}
</style>
</head>
<body onclick="reMoveLayerWait(this);">
	<meta name="renderer" content="webkit" />
<link href="https://hz.qk365.com/css/reset.css?version=20170912" rel="stylesheet" type="text/css">
<link href="https://hz.qk365.com/css/style.css?version=201906141" rel="stylesheet" type="text/css">
<link href="https://hz.qk365.com/css/head.css?version=20181025" rel="stylesheet" type="text/css">
<link href="https://hz.qk365.com/css/footer.css?version=20181026" rel="stylesheet" type="text/css">
<link href="https://hz.qk365.com/css/user.css?version=20180103" rel="stylesheet" type="text/css">
<link rel="stylesheet" href="https://hz.qk365.com/css/packet.css?version=20180124" type="text/css">

<script type="text/javascript">
	function checkMobile() {
		return navigator.userAgent
						.match(/iphone|android|phone|mobile|wap|netfront|x11|java|opera mobi|opera mini|ucweb|windows ce|symbian|symbianos|series|webos|sony|blackberry|dopod|nokia|samsung|palmsource|xda|pieplus|meizu|midp|cldc|motorola|foma|docomo|up.browser|up.link|blazer|helio|hosin|huawei|novarra|coolpad|webos|techfaith|palmsource|alcatel|amoi|ktouch|nexian|ericsson|philips|sagem|wellcom|bunjalloo|maui|smartphone|iemobile|spice|bird|zte-|longcos|pantech|gionee|portalmmm|jig browser|hiptop|benq|haier|^lct|320x320|240x320|176x220/i) != null;
	}
	(function() {
		cur_url = document.URL;
		if (checkMobile()) {
			if (cur_url=="https://www.qk365.com/"||cur_url=="https://www.qk365.com") {
				window.location.href = "https://i.qk365.com/";
			} else if (cur_url=="https://sz.qk365.com/"||cur_url=="https://sz.qk365.com") {
				window.location.href = "https://i.qk365.com/su";
			} else if (cur_url=="https://hz.qk365.com/"||cur_url=="https://hz.qk365.com") {
				window.location.href = "https://i.qk365.com/hz";
			} else if (cur_url=="https://bj.qk365.com/"||cur_url=="https://bj.qk365.com") {
				window.location.href = "https://i.qk365.com/bj";
			} else if (cur_url=="https://jx.qk365.com/"||cur_url=="https://jx.qk365.com") {
				window.location.href = "https://i.qk365.com/jx";
			} else if (cur_url=="https://nj.qk365.com/"||cur_url=="https://nj.qk365.com") {
				window.location.href = "https://i.qk365.com/nj";
			} else if (cur_url=="https://wh.qk365.com/"||cur_url=="https://wh.qk365.com") {
				window.location.href = "https://i.qk365.com/wh";
			}
		}
	})();
</script>

<div class="headNav">
    <div class="headLeft">
        <a class="logo" title="杭州租房" href="https://hz.qk365.com/"><img src="https://hz.qk365.com/images/logo.png" alt="杭州租房" /></a>
        <div class="popup">杭州</div>
				<div class="popupHide">
				<a href="https://www.qk365.com" title="上海租房" onclick="this.href=getCityChangeUrl('https://www.qk365.com');">上海</a>
				<a href="https://sz.qk365.com" title="苏州租房" onclick="this.href=getCityChangeUrl('https://sz.qk365.com');">苏州</a>
				<a href="https://hz.qk365.com" title="杭州租房" onclick="this.href=getCityChangeUrl('https://hz.qk365.com');">杭州</a>
				<a href="https://bj.qk365.com" title="北京租房" onclick="this.href=getCityChangeUrl('https://bj.qk365.com');">北京</a>
				<a href="https://jx.qk365.com" title="嘉兴租房" onclick="this.href=getCityChangeUrl('https://jx.qk365.com');">嘉兴</a>
				<a href="https://nj.qk365.com" title="南京租房" onclick="this.href=getCityChangeUrl('https://nj.qk365.com');">南京</a>
				<a href="https://wh.qk365.com" title="武汉租房" onclick="this.href=getCityChangeUrl('https://wh.qk365.com');">武汉</a>
				</div>
		</div>
    
    <div class="headRight">
        <div class="phone">
			<p class="ph1"><img src="https://hz.qk365.com/images/icon01.png" alt="杭州租房看房热线" />&nbsp;看房热线：&nbsp;8:00~22:00	</p>
			<p class="ph2">400-1737-365</p>
		</div>

        <ul class="subnav">
            <li>
                <button class="subnav-top">房屋出租</button>
                <div class="dropnav">
                    <a href="https://hz.qk365.com/list" title="杭州轻松找房">轻松找房</a>
                    <a href="https://hz.qk365.com/xiaoqu" title="杭州小区租房">小区租房</a>
                    <a href="https://hz.qk365.com/todaySpecial" title="杭州今日特惠">今日特惠</a>
                    <a href="https://hz.qk365.com/bus" title="杭州公交沿线租房">公交沿线租房</a>
                </div>
            </li>
            <li>
                <a href="https://hz.qk365.com/map" target="_blank" class="subnav-top" title="杭州租房地图找房">地图找房</a>
            </li>
            <li>
                <a href="https://hz.qk365.com/fwtg" target="_blank" rel="nofollow" class="subnav-top" title="杭州租房房屋托管">房屋托管</a>
            </li>
            <li>
                <button class="subnav-top">商务合作</button>
                <div class="dropnav">
                    <a href="https://hz.qk365.com/supplier/index" rel="nofollow" title="杭州租房商务合作">商务合作</a>
                    <a href="https://hz.qk365.com/to/jsp_government" rel="nofollow" title="杭州政府视窗">政府视窗</a>
                </div>
            </li>
            <li>
                <button class="subnav-top">青客快讯</button>
                <div class="dropnav">
                    <a href="https://hz.qk365.com/qkkx/index.html" title="杭州租房">青客快讯首页</a>
                    <a href="https://hz.qk365.com/qkkx/zfgl/index.html" title="杭州租房找房攻略">找房攻略</a>
                    <a href="https://hz.qk365.com/qkkx/hydt/index.html" title="杭州租房行业动态">行业动态</a>
                    <a href="https://hz.qk365.com/qkkx/ssrd/index.html" title="杭州租房时事热点">时事热点</a>
                    <a href="https://hz.qk365.com/qkkx/sqgl/index.html" title="杭州租房省钱攻略">省钱攻略</a>
                    <a href="https://hz.qk365.com/qkkx/bmxx/index.html" title="杭州租房便民信息">便民信息</a>
                    <a href="https://hz.qk365.com/qkkx/zzhd/index.html" title="杭州租房组织活动">组织活动</a>
                    <a href="https://hz.qk365.com/mail.do" rel="nofollow" title="鸡毛信">鸡毛信</a>
                    </div>
            </li>
            <li>
                <button class="subnav-top">移动青客</button>
                <div class="dropnav">
                    <a href="https://www.qk365.com/news/APP/index.html">下载APP</a>
                    <a href="https://i.qk365.com/hz">进入手机官网</a>
						</div>
            </li>
            
            <li class="" id="noLogin">
                <a href="https://hz.qk365.com/security/register" id="loginli" class="subnav-top" rel="nofollow">注册登录<em></em></a>
            </li>
            <li class="userico" id="loginIn" style="display: none">
                <a href="javascript:;" class="subnav-top pepSnapLogin"><i></i>注册登录</a>
                <div class="dropnav">
                    <a href="javascript:;" id="topMyData">我的资料</a>
					<a href="https://hz.qk365.com/security/reservation.do">我的预约</a>
					<a href="https://hz.qk365.com/security/subscribe.do">我的订阅</a>
					<a href="https://hz.qk365.com/security/userCouponsActivities.do">我的优惠券</a>
					<a href="https://hz.qk365.com/security/collection.do">我的收藏</a>
					<a href="javascript:;" id="logout">退出</a>
                </div>
            </li>
            
        </ul>
        <div class="clearfix"></div>
    </div>
</div>
<div class="easyTopSel">
		<div class="w1170 clearfix">
			<div class="easyCurve">
		<span>您当前的位置：</span>
		<div id="topnanv">
			<div id="anvlfteb">
				
				<div class="posbox">
						<a title="杭州租房" href="https://hz.qk365.com">杭州租房</a> <i></i>
							</div>
				<em>></em>
					<div class="posbox">
						<a title="轻松找房" href="https://hz.qk365.com/list">轻松找房</a>
								<i></i>
								</div>
				</div>
			<div id="seledbox" class="posiabox">
			<div class="area areaCur">
						<a title="上海租房" href="https://www.qk365.com" target="_blank">上海租房</a>
						<a title="苏州租房" href="https://sz.qk365.com" target="_blank">苏州租房</a>
						<a title="北京租房" href="https://bj.qk365.com" target="_blank">北京租房</a>
						<a title="嘉兴租房" href="https://jx.qk365.com" target="_blank">嘉兴租房</a>
						<a title="南京租房" href="https://nj.qk365.com" target="_blank">南京租房</a>
						<a title="武汉租房" href="https://wh.qk365.com" target="_blank">武汉租房</a>
						</div>
				<div class="area">
						<a title="小区找房" href="https://hz.qk365.com/xiaoqu" target="_blank">小区找房</a>
								<a title="地图找房" href="https://hz.qk365.com/map" target="_blank">地图找房</a>
								<a title="今日特惠" href="https://hz.qk365.com/todaySpecial" target="_blank">今日特惠</a>
								<a title="公交沿线租房" href="https://hz.qk365.com/bus/" target="_blank">公交沿线租房</a>
								</div>
				</div>
		</div>
		<div class="clear"></div>
	</div>
<div class="easySoBox clearfix">
				<div class="easySo">
					<span class="easySoTit fL">房间价格：</span> <span
						class="easySoCon priceCon fL"> <a href="javascript:price('');" rel="nofollow"><em
							  class="cur" >不限</em></a>
						<a title="500元以下租房" href="https://hz.qk365.com/list/r0-t500"
								style="color: #666;" onclick="price('500元以下','76');" rel="nofollow"><em
								>500元以下</em></a>
						<a title="500-700元租房" href="https://hz.qk365.com/list/r500-t700"
								style="color: #666;" onclick="price('500-700元','27');" rel="nofollow"><em
								>500-700元</em></a>
						<a title="700-1000元租房" href="https://hz.qk365.com/list/r700-t1000"
								style="color: #666;" onclick="price('700-1000元','28');" rel="nofollow"><em
								>700-1000元</em></a>
						<a title="1000-1500元租房" href="https://hz.qk365.com/list/r1000-t1500"
								style="color: #666;" onclick="price('1000-1500元','29');" rel="nofollow"><em
								>1000-1500元</em></a>
						<a title="1500-2000元租房" href="https://hz.qk365.com/list/r1500-t2000"
								style="color: #666;" onclick="price('1500-2000元','30');" rel="nofollow"><em
								>1500-2000元</em></a>
						<a title="2000-3000元租房" href="https://hz.qk365.com/list/r2000-t3000"
								style="color: #666;" onclick="price('2000-3000元','73');" rel="nofollow"><em
								>2000-3000元</em></a>
						<a title="3000元以上租房" href="https://hz.qk365.com/list/r3000"
								style="color: #666;" onclick="price('3000元以上','31');" rel="nofollow"><em
								>3000元以上</em></a>
						</span> <span class="priceAuto fR"><em>自定义：</em> <input
						name="priceL" maxlength="6" class="priceInput" type="text"
						id="priceL"
						value="" />
						<em>到</em> <input name="priceH" maxlength="6" class="priceInput"
						type="text" class="dd_input" id="priceH"
						value="" />
						<input type="button" value="确  定" id="bt_sub" class="priceSub"/></span>
				</div>
				<div class="easySo" id="easySo">
					<span class="easySoTit fL">行政区域：</span> <span
						class="easySoCon areaCon fL"> <a title="杭州租房"
						href="javascript:condition('prcId','');"> <em
							  class="cur" >不限</em>
					</a> <a title="上城区租房"
								href="https://hz.qk365.com/list/a47" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','47');"> <em
								>
									上城区</em>
							</a>
						<a title="下城区租房"
								href="https://hz.qk365.com/list/a48" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','48');"> <em
								>
									下城区</em>
							</a>
						<a title="江干区租房"
								href="https://hz.qk365.com/list/a49" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','49');"> <em
								>
									江干区</em>
							</a>
						<a title="拱墅区租房"
								href="https://hz.qk365.com/list/a50" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','50');"> <em
								>
									拱墅区</em>
							</a>
						<a title="西湖区租房"
								href="https://hz.qk365.com/list/a51" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','51');"> <em
								>
									西湖区</em>
							</a>
						<a title="滨江区租房"
								href="https://hz.qk365.com/list/a52" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','52');"> <em
								>
									滨江区</em>
							</a>
						<a title="萧山区租房"
								href="https://hz.qk365.com/list/a53" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','53');"> <em
								>
									萧山区</em>
							</a>
						<a title="余杭区租房"
								href="https://hz.qk365.com/list/a54" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','54');"> <em
								>
									余杭区</em>
							</a>
						<a title="桐庐县租房"
								href="https://hz.qk365.com/list/a55" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','55');"> <em
								>
									桐庐县</em>
							</a>
						<a title="淳安县租房"
								href="https://hz.qk365.com/list/a56" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','56');"> <em
								>
									淳安县</em>
							</a>
						<a title="建德市租房"
								href="https://hz.qk365.com/list/a57" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','57');"> <em
								>
									建德市</em>
							</a>
						<a title="富阳市租房"
								href="https://hz.qk365.com/list/a58" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','58');"> <em
								>
									富阳市</em>
							</a>
						<a title="临安市租房"
								href="https://hz.qk365.com/list/a59" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','59');"> <em
								>
									临安市</em>
							</a>
						</a>
					</span>
				</div>
				<div class="easySo">
					<span class="easySoTit fL">地铁沿线：</span> <span
						class="easySoCon metroSoList fL"> <a title="杭州租房"
						href="javascript:condition('subway','');"> <i
							  class="cur"  >不限</i>
					</a> <a title="1号线租房" href="https://hz.qk365.com/list/s19"
								style="color: #666;"
								onclick="condition('subway','19');"> <em
								>
									1号线</em>
							</a>
						<a title="2号线租房" href="https://hz.qk365.com/list/s20"
								style="color: #666;"
								onclick="condition('subway','20');"> <em
								>
									2号线</em>
							</a>
						<a title="4号线租房" href="https://hz.qk365.com/list/s21"
								style="color: #666;"
								onclick="condition('subway','21');"> <em
								>
									4号线</em>
							</a>
						</span>
				</div>
				<div class="easySo">
					<span class="easySoTit fL">房间户型：</span> <span
						class="easySoCon roomDoor fL"> <a href="javascript:condition('romType','');" rel="nofollow"> <em
							 class="cur"  >不限</em>
					</a> <a title="杭州独卫租房" href="https://hz.qk365.com/list/f1"
								style="color: #666;"
								onclick="condition('romType','1');" rel="nofollow"> <em
								>
									独卫</em>
							</a>
						<a title="杭州单间租房" href="https://hz.qk365.com/list/f2"
								style="color: #666;"
								onclick="condition('romType','2');" rel="nofollow"> <em
								>
									单间</em>
							</a>
						<a title="杭州整租租房" href="https://hz.qk365.com/list/f3"
								style="color: #666;"
								onclick="condition('romType','3');" rel="nofollow"> <em
								>
									整租</em>
							</a>
						</span>
				</div>
				<div class="easySo easySoNo">
					<span class="easySoTit fL">可租日期：</span> <span
						class="easySoCon roomDoor fL"> <a href="javascript:queryRent('');"> <em
							 class="cur" >不限</em>
					</a> <a style="color: #666;"
						href="javascript:queryRent('anyTimeRent');"> <em
							>立即可租</em>
					</a> <a style="color: #666;"
						href="javascript:queryRent('oneWeekRent');"> <em
							>一周内可租</em>
					</a> <a style="color: #666;"
						href="javascript:queryRent('twoWeekRent');"> <em
							>两周内可租</em>
					</a> <a style="color: #666;"
						href="javascript:queryRent('oneMonthRent');"> <em
							>一月内可租</em>
					</a><a style="color: #666;"
						   href="javascript:queryRent('sixtyDayRent');"> <em
						>两月内可租</em>
					</a>
					</span>
				</div>
				</div>
			<div class="easySort clearfix">
				<div class="easySo">
					<a onclick="javascript:sort('romVacantDays');"> <span
						class="easySoTit fL"> 默认排序： </span>
					</a> <span class="easySoCon roomDoor fL"> <a style="color: #666;" href="javascript:sort('showPrice');">
							<em
							>价格</em>
					</a> <a style="color: #666;" href="javascript:sort('romArea');"> <em
							>面积</em>
					</a> <a style="color: #666;" href="javascript:sort('cucSubwayDistance');"> <em
							>距地铁</em>
					</a> <a style="color: #666;" href="javascript:sort('romView');"> <em
							>浏览次数</em>
					</a>
							<a style="color: #666;" href="javascript:sort('cucVideoUrl');">
								<em id="new"
								>视频看房
									</em>
							</a>
					</span>
					<div class="SortSel fR">
						<em>总共2585间房间</em> <span class="sortInpLay">
							<input type="text" class="sortinText" id="houseRoad" onkeydown="keyUpSearch('qszf')"
								   onfocus="addLayer(this);"
							
							 value="输入区域、地铁、小区名" onfocus="if (this.value =='输入区域、地铁、小区名'){this.value =''}" onblur="if (this.value ==''){this.value='输入区域、地铁、小区名';$('.delete').hide();}"
						 
						 maxlength="50" />
						<input type="hidden" id="houseRoad_b" value="">
						<input type="hidden" id="stamp" value="spread">
						<em class="delete"></em>
						<input type="button" onclick="keySearch('qszf');" value="" class="sortSub">
						<ul class="jeasySearch blsearch hide" id="resultList">
						</ul>
						<ul class="easySearch blsearch hide" id="hotSearchList">
						</ul>
						</span>
					</div>
				</div>
			</div>
			
			<div class="preference">
	<div class="limit">
		<h4>限时特惠</h4>
		<a title="杭州租房" href="https://hz.qk365.com/todaySpecial" target="_blank">
			<img src="https://hz.qk365.com/images/odds-more.png"
				 alt="杭州租房"></a>
	</div>
	<div class="imgBox">
		<div class="Imgscrollbox" id="box0">
			<ul class="boxList">
				<li>
						<a title="杭州之江家园四区租房" class="roomPic" href="https://hz.qk365.com/room/60092" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/0F/66/CgoKaFy71CGAEXLfAAB3Mu7TGR4781.jpg" title="转塘之江家园四区租房"
										 alt="杭州租房"
										 onerror="defaultPic(this,'https://hz.qk365.com/','0')">
								<div class="playSmall"><img src="https://hz.qk365.com/images/play02.png"></div>   <!-- 新添播放按钮 -->
							<p>
									<span><img src="https://hz.qk365.com/images/special_price.png" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="西湖区租房" class="addArea" href="https://hz.qk365.com/list/a51" target="_blank">西湖区</a>
                                    <span>
                                        <i><img src="https://hz.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://hz.qk365.com/xiaoqu/v23828" target="_blank" title="之江家园四区租房">之江家园四区</a>
                                    </span>
							</div>
							<p>
									<i>
										1163</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				<li>
						<a title="杭州之江家园五区租房" class="roomPic" href="https://hz.qk365.com/room/56636" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/5E/51/CgoKZ10InDSATPDIAABxojSeUvA845.jpg" title="转塘之江家园五区租房"
										 alt="杭州租房"
										 onerror="defaultPic(this,'https://hz.qk365.com/','0')">
								<div class="playSmall"><img src="https://hz.qk365.com/images/play02.png"></div>   <!-- 新添播放按钮 -->
							<p>
									<span><img src="https://hz.qk365.com/images/special_price.png" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="西湖区租房" class="addArea" href="https://hz.qk365.com/list/a51" target="_blank">西湖区</a>
                                    <span>
                                        <i><img src="https://hz.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://hz.qk365.com/xiaoqu/v23738" target="_blank" title="之江家园五区租房">之江家园五区</a>
                                    </span>
							</div>
							<p>
									<i>
										1213</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				<li>
						<a title="杭州胜稼红星嘉园四区租房" class="roomPic" href="https://hz.qk365.com/room/77499" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/9C/6F/CgoKZ1xF7YWAa9F3AABYDM9PaFE862.jpg" title="乔司胜稼红星嘉园四区租房"
										 alt="杭州租房"
										 onerror="defaultPic(this,'https://hz.qk365.com/','0')">
								<div class="playSmall"><img src="https://hz.qk365.com/images/play02.png"></div>   <!-- 新添播放按钮 -->
							<p>
									<span><img src="https://hz.qk365.com/images/special_price.png" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="余杭区租房" class="addArea" href="https://hz.qk365.com/list/a54" target="_blank">余杭区</a>
                                    <span>
                                        <i><img src="https://hz.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://hz.qk365.com/xiaoqu/v24597" target="_blank" title="胜稼红星嘉园四区租房">胜稼红星嘉园四区</a>
                                    </span>
							</div>
							<p>
									<i>
										1346</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				<li>
						<a title="杭州胜稼红星嘉园三区租房" class="roomPic" href="https://hz.qk365.com/room/77388" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/9D/02/CgoKaFxGAfCAAzW_AABavtGpEXg867.jpg" title="乔司胜稼红星嘉园三区租房"
										 alt="杭州租房"
										 onerror="defaultPic(this,'https://hz.qk365.com/','0')">
								<div class="playSmall"><img src="https://hz.qk365.com/images/play02.png"></div>   <!-- 新添播放按钮 -->
							<p>
									<span><img src="https://hz.qk365.com/images/special_price.png" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="余杭区租房" class="addArea" href="https://hz.qk365.com/list/a54" target="_blank">余杭区</a>
                                    <span>
                                        <i><img src="https://hz.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://hz.qk365.com/xiaoqu/v24596" target="_blank" title="胜稼红星嘉园三区租房">胜稼红星嘉园三区</a>
                                    </span>
							</div>
							<p>
									<i>
										1363</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				<li>
						<a title="杭州丰润家园租房" class="roomPic" href="https://hz.qk365.com/room/86849" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/FF/54/CgoKZ1ysUN-ABpToAABkUEzjZPE401.jpg" title="北干丰润家园租房"
										 alt="杭州租房"
										 onerror="defaultPic(this,'https://hz.qk365.com/','0')">
								<div class="playSmall"><img src="https://hz.qk365.com/images/play02.png"></div>   <!-- 新添播放按钮 -->
							<p>
									<span><img src="https://hz.qk365.com/images/special_price.png" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="萧山区租房" class="addArea" href="https://hz.qk365.com/list/a53" target="_blank">萧山区</a>
                                    <span>
                                        <i><img src="https://hz.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://hz.qk365.com/xiaoqu/v24756" target="_blank" title="丰润家园租房">丰润家园</a>
                                    </span>
							</div>
							<p>
									<i>
										1598</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				</ul>
		</div>
	</div>
	<a class="gor" id="gor0"><img src="https://hz.qk365.com/images/nextSnap.png" alt="杭州租房"></a>
</div>
<form id="roomForm" name="roomForm" method="post"
				action="https://hz.qk365.com/list/">
				<input name="queryDto.priceFrom" id="priceFrom" type="hidden"
		value="" />
	<input name="queryDto.priceTo" id="priceTo" type="hidden"
		value="" />
	<input name="queryDto.priceId" id="priceId" type="hidden"
		value="" />
	<input name="queryDto.prcId" id="prcId" type="hidden"
		value="" />
	<input name="queryDto.cellArea" id="cellArea" type="hidden"
		value="" />
	<input name="queryDto.romType" id="romType" type="hidden"
		value="" />
	<input name="queryDto.romAds" id="romAds" type="hidden"
		value="" />
	<input name="queryDto.subway" id="subway" type="hidden"
		value="" />
		<input name="queryDto.station" id="station" type="hidden"
		value="" />
	<input name="queryDto.stationCode" id="stationCode" type="hidden"
		value="" />
	<input name="queryDto.currentPage" id="currentPage" type="hidden"
		value="1" />
	<input name="queryDto.pageSize" id="pageSize" type="hidden"
		value="21" />
	
	<input name="queryDto.orderByField" id="orderByField" type="hidden"
		value="" />
		<input name="queryDto.orderShort" id="orderShort" type="hidden"
		value="" />
	
	<input name="queryDto.sortDirection" id="sortDirection" type="hidden"
		value="" />
	
	<input name="queryDto.pinyin" id="pinyin" type="hidden"
		value="" />
	<input name="queryDto.village" id="village" type="hidden"
		value="" />
	
	<input name="queryDto.villageId" id="villageId" type="hidden"
		value="" />
	
	<input name="queryDto.order" id="order" type="hidden"
		value="" />
	<input name="queryDto.roomCode" id="roomCode" type="hidden"
		value="" />

	<input name="expectedCheckinTime" id="expectedCheckinTime"
		type="hidden" value="" />
	<input name="romAddress" id="romAddress" type="hidden" value="" />
    <input name="queryDto.rentDateName" id="rentDateName" type="hidden"
	   value="" />
    <input name="queryDto.activityId" id="activityId" type="hidden"
	   value="" />
    <input name="queryDto.activityLabelName" id="activityLabelName" type="hidden"
	   value="" />
<input name="ajax" id="priceFrom" type="hidden" value="ajax" />
			</form>
		</div>
	</div>
	<div class="easyWarp">
		<div class="w1170 clearfix">
			<ul class="easyList">
				<li>
					<a target="_blank" title="杭州转塘家园图"
						href="https://hz.qk365.com/room/80385">
							<img src="https://hz.qk365.com/images/noPic_Big0.jpg" 
							alt="杭州转塘家园图" title="杭州转塘家园图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【西湖区】转塘家园 精装白领公寓 朝南朝南单间出租 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:2038</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="西湖区租房" href="https://hz.qk365.com/list/a51">西湖区</a>-<a title="转塘租房" href="https://hz.qk365.com/list/a51-k505">转塘</a>-<a title="转塘家园租房" href="https://hz.qk365.com/xiaoqu/v27298">转塘家园</a>租房 5/18层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>朝南</i>
		<i>飘窗</i>
		<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>1289</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10180734" title="转塘东租房">转塘东</a>
						 		<span>&nbsp;公交站约278米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州之江家园五区图"
						href="https://hz.qk365.com/room/56636">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/5E/51/CgoKZ10InDSATPDIAABxojSeUvA845.jpg" 
							alt="杭州之江家园五区图" title="杭州之江家园五区图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【西湖区】转塘周边 之江家园五区 精装白领公寓朝南主卧出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2269</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="西湖区租房" href="https://hz.qk365.com/list/a51">西湖区</a>-<a title="转塘租房" href="https://hz.qk365.com/list/a51-k505">转塘</a>-<a title="之江家园五区租房" href="https://hz.qk365.com/xiaoqu/v23738">之江家园五区</a>租房 23/35层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>主卧</i>
		<i>朝南</i>
		<i>飘窗</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1213</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10184310" title="象山租房">象山</a>
						 		<span>&nbsp;公交站约453米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州之江家园四区图"
						href="https://hz.qk365.com/room/60092">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/0F/66/CgoKaFy71CGAEXLfAAB3Mu7TGR4781.jpg" 
							alt="杭州之江家园四区图" title="杭州之江家园四区图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【西湖区】杜家浦路   之江家园四区  精装白领公寓  朝南主卧出租   配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2439</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="西湖区租房" href="https://hz.qk365.com/list/a51">西湖区</a>-<a title="转塘租房" href="https://hz.qk365.com/list/a51-k505">转塘</a>-<a title="之江家园四区租房" href="https://hz.qk365.com/xiaoqu/v23828">之江家园四区</a>租房 1/11层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>主卧</i>
		<i>朝南</i>
		<i>飘窗</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1163</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10184310" title="象山租房">象山</a>
						 		<span>&nbsp;公交站约161米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州胜稼红星嘉园三区图"
						href="https://hz.qk365.com/room/77388">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9D/02/CgoKaFxGAfCAAzW_AABavtGpEXg867.jpg" 
							alt="杭州胜稼红星嘉园三区图" title="杭州胜稼红星嘉园三区图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】1号线 乔司南站 胜稼红星嘉园三区 精装白领公寓朝南阳台房 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2431</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="乔司租房" href="https://hz.qk365.com/list/a54-k402">乔司</a>-<a title="胜稼红星嘉园三区租房" href="https://hz.qk365.com/xiaoqu/v24596">胜稼红星嘉园三区</a>租房 4/16层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>阳台</i>
		<i>朝南</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1363</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s19" title="1号线租房">1号线</a>
		                   	<a href="https://hz.qk365.com/list/s19-e19022" title="乔司南租房">乔司南</a>
		                   	<span>约950米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10180839" title="三卫村租房">三卫…</a>
						 		<span>&nbsp;公交站约169米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州胜稼红星嘉园四区图"
						href="https://hz.qk365.com/room/77499">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9C/6F/CgoKZ1xF7YWAa9F3AABYDM9PaFE862.jpg" 
							alt="杭州胜稼红星嘉园四区图" title="杭州胜稼红星嘉园四区图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】1号线 乔司南站 胜稼红星嘉园二区 精装白领公寓朝南阳台房出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2442</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="乔司租房" href="https://hz.qk365.com/list/a54-k402">乔司</a>-<a title="胜稼红星嘉园四区租房" href="https://hz.qk365.com/xiaoqu/v24597">胜稼红星嘉园四区</a>租房 10/15层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>阳台</i>
		<i>朝南</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1346</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s19" title="1号线租房">1号线</a>
		                   	<a href="https://hz.qk365.com/list/s19-e19022" title="乔司南租房">乔司南</a>
		                   	<span>约950米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10180839" title="三卫村租房">三卫…</a>
						 		<span>&nbsp;公交站约169米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州大华海派风景图"
						href="https://hz.qk365.com/room/85705">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9F/CF/CgoKaFxGf-SARM5vAAB1as5cP9g678.jpg" 
							alt="杭州大华海派风景图" title="杭州大华海派风景图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】地铁2号线 墩祥街站 大华海派风景 精装白领公寓 朝南次卧带飘窗出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2736</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="勾庄租房" href="https://hz.qk365.com/list/a54-k408">勾庄</a>-<a title="大华海派风景租房" href="https://hz.qk365.com/xiaoqu/v24277">大华海派风景</a>租房 12/18层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>朝南</i>
		<i>飘窗</i>
		<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>1831</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>&nbsp;</span><a href="https://hz.qk365.com/list/s20" title="2号线租房">2号线</a>
		                   	<a href="https://hz.qk365.com/list/s20-e20628" title="墩祥街租房">墩祥街；</a>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10185137" title="通运路杭行路口租房">通运…</a>
						 		<span>&nbsp;公交站约445米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州淮矿东元府图"
						href="https://hz.qk365.com/room/66783">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/EA/5F/CgoKZ1yZxkGAAJR6AACI6rt0L44317.jpg" 
							alt="杭州淮矿东元府图" title="杭州淮矿东元府图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【江干区】地铁1号线   彭埠站  淮矿东元府  精装白领公寓  朝南主卧带阳台出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2959</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="江干区租房" href="https://hz.qk365.com/list/a49">江干区</a>-<a title="城东新城租房" href="https://hz.qk365.com/list/a49-k443">城东新城</a>-<a title="淮矿东元府租房" href="https://hz.qk365.com/xiaoqu/v25712">淮矿东元府</a>租房 20/22层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>主卧</i>
		<i>阳台</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>2099</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s21" title="4号线租房">4号线</a>
		                   	<a href="https://hz.qk365.com/list/s21-e19017" title="彭埠租房">彭埠</a>
		                   	<span>约816米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10186247" title="叶家塘租房">叶家…</a>
						 		<span>&nbsp;公交站约204米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州东祥元府图"
						href="https://hz.qk365.com/room/73494">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/E2/68/CgoKaFyRtlGAQ2eDAAByr_7jphA396.jpg" 
							alt="杭州东祥元府图" title="杭州东祥元府图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【江干区】1/4号线 彭埠站 东祥元府 精装白领公寓朝南主卧出租   配备齐全   拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:2978</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="江干区租房" href="https://hz.qk365.com/list/a49">江干区</a>-<a title="彭埠租房" href="https://hz.qk365.com/list/a49-k434">彭埠</a>-<a title="东祥元府租房" href="https://hz.qk365.com/xiaoqu/v24513">东祥元府</a>租房 11/22层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>主卧</i>
		<i>朝南</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>2019</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s21" title="4号线租房">4号线</a>
		                   	<a href="https://hz.qk365.com/list/s21-e19017" title="彭埠租房">彭埠</a>
		                   	<span>约849米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10180825" title="高速彭埠口租房">高速…</a>
						 		<span>&nbsp;公交站约182米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州丰润家园图"
						href="https://hz.qk365.com/room/86849">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/FF/54/CgoKZ1ysUN-ABpToAABkUEzjZPE401.jpg" 
							alt="杭州丰润家园图" title="杭州丰润家园图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【萧山区】地铁2号线 建设一路站 丰润家园 精装白领公寓 朝南次卧出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2660</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="萧山区租房" href="https://hz.qk365.com/list/a53">萧山区</a>-<a title="北干租房" href="https://hz.qk365.com/list/a53-k419">北干</a>-<a title="丰润家园租房" href="https://hz.qk365.com/xiaoqu/v24756">丰润家园</a>租房 17/26层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>朝南</i>
		<i>飘窗</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1598</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s20" title="2号线租房">2号线</a>
		                   	<a href="https://hz.qk365.com/list/s20-e2007" title="建设一路租房">建设一路</a>
		                   	<span>约1258米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10635085" title="博学路金鸡路口租房">博学…</a>
						 		<span>&nbsp;公交站约95米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州胜稼红星嘉园二区图"
						href="https://hz.qk365.com/room/76033">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/36/8A/CgoKaFzjmRCALgoVAABKxprkFU0339.jpg" 
							alt="杭州胜稼红星嘉园二区图" title="杭州胜稼红星嘉园二区图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】地铁1号线  乔司南站  胜稼红星嘉园二区  精装白领公寓  朝南主卧带阳台出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2398</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="乔司租房" href="https://hz.qk365.com/list/a54-k402">乔司</a>-<a title="胜稼红星嘉园二区租房" href="https://hz.qk365.com/xiaoqu/v19320">胜稼红星嘉园二区</a>租房 14/16层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>主卧</i>
		<i>阳台</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1346</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s19" title="1号线租房">1号线</a>
		                   	<a href="https://hz.qk365.com/list/s19-e19022" title="乔司南租房">乔司南</a>
		                   	<span>约950米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10180839" title="三卫村租房">三卫…</a>
						 		<span>&nbsp;公交站约169米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州越秀星汇尚城图"
						href="https://hz.qk365.com/room/53250">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/1B/E6/CgoKaFzH5x2AcVIYAAB1gjtkT-U820.jpg" 
							alt="杭州越秀星汇尚城图" title="杭州越秀星汇尚城图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】2号线 钱江路站 越秀星汇尚城	 精装白领公寓 单间出租 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:2526</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="良渚租房" href="https://hz.qk365.com/list/a54-k405">良渚</a>-<a title="越秀星汇尚城租房" href="https://hz.qk365.com/xiaoqu/v23474">越秀星汇尚城</a>租房 5/19层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1345</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10185724" title="运河广告产业园租房">运河广告产业园</a>
						 		<span>&nbsp;公交站约469米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州越秀星汇尚城图"
						href="https://hz.qk365.com/room/54791">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/1A/60/CgoKZ1zGkDWAOSEJAABtV6VJO_k841.jpg" 
							alt="杭州越秀星汇尚城图" title="杭州越秀星汇尚城图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】2号线 钱江路站 越秀星汇尚城 精装白领公寓 单间次卧出租 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:2508</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="良渚租房" href="https://hz.qk365.com/list/a54-k405">良渚</a>-<a title="越秀星汇尚城租房" href="https://hz.qk365.com/xiaoqu/v23474">越秀星汇尚城</a>租房 7/23层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1325</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10185724" title="运河广告产业园租房">运河广告产业园</a>
						 		<span>&nbsp;公交站约469米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州风雅乐府图"
						href="https://hz.qk365.com/room/50963">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/1B/F0/CgoKZ1zH6fiAAg3VAAB58Az6Oz8187.jpg" 
							alt="杭州风雅乐府图" title="杭州风雅乐府图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】良渚街道 风雅乐府 精装白领公寓主卧带阳台出租  配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2801</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="勾庄租房" href="https://hz.qk365.com/list/a54-k408">勾庄</a>-<a title="风雅乐府租房" href="https://hz.qk365.com/xiaoqu/v23473">风雅乐府</a>租房 6/29层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>主卧</i>
		<i>阳台</i>
		<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>2106</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10185135" title="好运路冯家浜路口租房">好运路冯家浜路口</a>
						 		<span>&nbsp;公交站约122米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州紫元尚堂府图"
						href="https://hz.qk365.com/room/64280">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/FD/5F/CgoKaFyqxmGAFcaEAABg1VDcU64441.jpg" 
							alt="杭州紫元尚堂府图" title="杭州紫元尚堂府图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【拱墅区】紫元尚堂府 精装青年公寓 朝南单间出租 近城市大学和瓜山家园</p>
					</div>
					<em class="fr0923">
						<b>原价:2420</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="拱墅区租房" href="https://hz.qk365.com/list/a50">拱墅区</a>-<a title="石祥路租房" href="https://hz.qk365.com/list/a50-k534">石祥路</a>-<a title="紫元尚堂府租房" href="https://hz.qk365.com/xiaoqu/v19356">紫元尚堂府</a>租房 12/18层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>朝南</i>
		<i>飘窗</i>
		<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1267</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10183109" title="瓜山租房">瓜山</a>
						 		<span>&nbsp;公交站约202米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州紫元尚堂府图"
						href="https://hz.qk365.com/room/64282">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/FD/60/CgoKZ1yqxp6AZF02AAB7eeGmgg8717.jpg" 
							alt="杭州紫元尚堂府图" title="杭州紫元尚堂府图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【拱墅区】紫元尚堂府 精装青年公寓 单间卧室出租 近城市大学和瓜山家园</p>
					</div>
					<em class="fr0923">
						<b>原价:2226</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="拱墅区租房" href="https://hz.qk365.com/list/a50">拱墅区</a>-<a title="石祥路租房" href="https://hz.qk365.com/list/a50-k534">石祥路</a>-<a title="紫元尚堂府租房" href="https://hz.qk365.com/xiaoqu/v19356">紫元尚堂府</a>租房 12/18层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>飘窗</i>
		<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1163</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10183109" title="瓜山租房">瓜山</a>
						 		<span>&nbsp;公交站约202米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州相寓图"
						href="https://hz.qk365.com/room/75038">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9D/E2/CgoKZ1xGJlGASGsNAAB8OlqgH7Q885.jpg" 
							alt="杭州相寓图" title="杭州相寓图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】1号线 临平站 荷田相寓 精装白领公寓 主卧带阳台出租</p>
					</div>
					<em class="fr0923">
						<b>原价:1697</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="临平租房" href="https://hz.qk365.com/list/a54-k407">临平</a>-<a title="相寓租房" href="https://hz.qk365.com/xiaoqu/v26247">相寓</a>租房 7/25层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>阳台</i>
		<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>1091</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10182459" title="荷禹路320国道口租房">荷禹路320国道口</a>
						 		<span>&nbsp;公交站约90米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州紫元尚堂府图"
						href="https://hz.qk365.com/room/53794">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/FD/61/CgoKZ1yqxxiAb3rXAAB2e2aXqhc427.jpg" 
							alt="杭州紫元尚堂府图" title="杭州紫元尚堂府图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【拱墅区】科祥街54号 紫元尚堂府 精装白领公寓朝北单间 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:2614</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="拱墅区租房" href="https://hz.qk365.com/list/a50">拱墅区</a>-<a title="石祥路租房" href="https://hz.qk365.com/list/a50-k534">石祥路</a>-<a title="紫元尚堂府租房" href="https://hz.qk365.com/xiaoqu/v19356">紫元尚堂府</a>租房 2/18层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>飘窗</i>
		<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1398</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10183109" title="瓜山租房">瓜山</a>
						 		<span>&nbsp;公交站约202米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州赞成乐山红叶图"
						href="https://hz.qk365.com/room/96808">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/0F/AE/CgoKZ1y780yAVVADAAB1f3_Pmhc778.jpg" 
							alt="杭州赞成乐山红叶图" title="杭州赞成乐山红叶图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】闲林 赞成乐山红叶 精装白领公寓 朝南卧室带阳台出租 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:1739</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="闲林租房" href="https://hz.qk365.com/list/a54-k398">闲林</a>-<a title="赞成乐山红叶租房" href="https://hz.qk365.com/xiaoqu/v28336">赞成乐山红叶</a>租房 19/20层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>阳台</i>
		<i>朝南</i>
		<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>1161</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10184501" title="闲林西租房">闲林西</a>
						 		<span>&nbsp;公交站约269米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州紫元尚堂府图"
						href="https://hz.qk365.com/room/53292">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9A/39/CgoKaFxFoZGAdX51AABieiQ34wI170.jpg" 
							alt="杭州紫元尚堂府图" title="杭州紫元尚堂府图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【拱墅区】二号线 丰潭路 紫元尚堂府 精装白领公寓朝南卧室 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:2479</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="拱墅区租房" href="https://hz.qk365.com/list/a50">拱墅区</a>-<a title="石祥路租房" href="https://hz.qk365.com/list/a50-k534">石祥路</a>-<a title="紫元尚堂府租房" href="https://hz.qk365.com/xiaoqu/v19356">紫元尚堂府</a>租房 3/23层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>朝南</i>
		<i>飘窗</i>
		<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1326</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10183109" title="瓜山租房">瓜山</a>
						 		<span>&nbsp;公交站约202米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州丰润家园图"
						href="https://hz.qk365.com/room/86832">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/3B/15/CgoKaFzo2SKAGWewAAByaee9Bag737.jpg" 
							alt="杭州丰润家园图" title="杭州丰润家园图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【萧山区】地铁2号线 建设一路站 丰润家园 精装白领公寓 朝南主卧出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2793</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="萧山区租房" href="https://hz.qk365.com/list/a53">萧山区</a>-<a title="北干租房" href="https://hz.qk365.com/list/a53-k419">北干</a>-<a title="丰润家园租房" href="https://hz.qk365.com/xiaoqu/v24756">丰润家园</a>租房 9/22层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>主卧</i>
		<i>朝南</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1598</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s20" title="2号线租房">2号线</a>
		                   	<a href="https://hz.qk365.com/list/s20-e2007" title="建设一路租房">建设一路</a>
		                   	<span>约1258米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10635085" title="博学路金鸡路口租房">博学…</a>
						 		<span>&nbsp;公交站约95米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州胜稼红星嘉园四区图"
						href="https://hz.qk365.com/room/78898">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9D/4A/CgoKZ1xGDBKASmsuAAB2fa3qe5g878.jpg" 
							alt="杭州胜稼红星嘉园四区图" title="杭州胜稼红星嘉园四区图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】1号线 乔司南站 胜稼红星嘉园 全新小区 精装全配 朝南主卧出租 拎包入住</p>
					</div>
					<em class="fr0923">
						<b>原价:2330</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="乔司租房" href="https://hz.qk365.com/list/a54-k402">乔司</a>-<a title="胜稼红星嘉园四区租房" href="https://hz.qk365.com/xiaoqu/v24597">胜稼红星嘉园四区</a>租房 11/15层
                                        <span>30天免费住，签约立减30天房租最高优惠3000元</span>
                                    	</span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>主卧</i>
		<i>朝南</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>1559</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s19" title="1号线租房">1号线</a>
		                   	<a href="https://hz.qk365.com/list/s19-e19022" title="乔司南租房">乔司南</a>
		                   	<span>约950米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10180839" title="三卫村租房">三卫…</a>
						 		<span>&nbsp;公交站约169米</span>
					 		</a>
					</div>
					</div>
				</li>
				</ul>
		</div>
		<p class="easyPage">
  <a href="https://hz.qk365.com/list/" onclick="javascript:void(0);return false;" class="prePage">&nbsp;</a>
    <a href="https://hz.qk365.com/list/" onclick="javascript:void(0);return false;" class="active">1</a>
        <a href="https://hz.qk365.com/list/p2" onclick="javascript:simpleTable.togglePage(2);return false;">2</a>
          <a href="https://hz.qk365.com/list/p3" onclick="javascript:simpleTable.togglePage(3);return false;">3</a>
          <a href="https://hz.qk365.com/list/p4" onclick="javascript:simpleTable.togglePage(4);return false;">4</a>
          <a href="https://hz.qk365.com/list/p5" onclick="javascript:simpleTable.togglePage(5);return false;">5</a>
          <a href="https://hz.qk365.com/list/p6" onclick="javascript:simpleTable.togglePage(6);return false;">6</a>
          <a href="https://hz.qk365.com/list/p7" onclick="javascript:simpleTable.togglePage(7);return false;">7</a>
          <a class="nextPage" href="https://hz.qk365.com/list/p2" onclick="javascript:simpleTable.togglePage(2);return false;">&nbsp;</a>
      </p>
</div>
<!-- 猜你喜欢 -->
	<div id="sidebarRig">
	<ul>
		<li>
			<span class="sidebarBox">
				<div class="sideFadeIn" style="display:none;">
					<div id="SideBox01">
                    	<div class="tit">
                        	<span><img  src="https://hz.qk365.com/images/Side/one-img.png" /></span>
                            <h3>关注青客</h3>
                        </div>
<!--                         <div class="scan"> -->
<!--                         	<p>扫描二维码</p> -->
<!--                             <p>关注我们</p> -->
<!--                         </div> -->
                        <div class="scan scan0">
                        	<p><img  src="https://hz.qk365.com/images/Side/wxImg02.png" /></p>
                        	<p>扫描二维码</p>
                            <p>下载APP</p>
                        </div>
					</div>
				</div>
				<img  src="https://hz.qk365.com/images/Side/one.png" width="53" height="45" class="sideFadeOut" />
			</span>
		</li>
        <li>
            <span class="sidebarBox">
                <div class="sideFadeIn" style="display:none;">
                    <div id="SideBox02">
                        <a  class="tit" href="https://hz.qk365.com/fwtg" target="_blank">
                            <span><img  src="https://hz.qk365.com/images/Side/two-img.png" /></span>
                            <h3>房屋托管</h3>
                        </a>
                    </div>
                </div>
                <img  src="https://hz.qk365.com/images/Side/two.png" width="53" height="45" class="sideFadeOut" />
            </span>
        </li>
        <li>
            <span class="sidebarBox">
                <div  class="sideFadeOut" style="display:block; position:relative; z-index:1;">
                    <div id="SideBox03">
                        <a  class="tit" target="_blank" href="https://pkt.zoosnet.net/LR/Chatpre.aspx?id=PKT38359414&lng=cn" >
                            <span><img src="https://hz.qk365.com/images/Side/three-img.png" /></span>
                            <h3>在线咨询</h3>
                        </a>
                    </div> 
                </div>
                <img src="https://hz.qk365.com/images/Side/three.png"  width="53" height="45" class="sideFadeIn" />
            </span>
        </li>
        
         <li>
            <span class="sidebarBox">
                <div class="sideFadeIn" style="display:none;">
                    <div id="SideBox04">
                    	<div class="tit">
                        	<span><img src="https://hz.qk365.com/images/Side/four-img.png" /></span>
                            <h3>租客需求</h3>
                        </div>
                        <div class="text">
                        	<textarea name="mydiyue" id="mydiyue" onclick="changeShowList(this,'https://hz.qk365.com/')">求租火车站附近房源</textarea>
                        </div>
                        <div class="submit">
                            <form id="mail">
                                <input type="submit" onclick="diyue_center('https://hz.qk365.com/security/subscribe.do');" value="确认" />
                            </form>
                        </div>
                    </div>
                </div>
            	<img src="https://hz.qk365.com/images/Side/four.png"  width="53" height="45" class="sideFadeOut" />
            </span>
        </li>
        
        <li id="sidebarTop">
            <span class="sidebarBox" id="top_btn">
                <div class="sideFadeIn" style="display:none">
                    <img src="https://hz.qk365.com/images/Side/five-1.png" width="124" height="45" />
                </div>
                <img src="https://hz.qk365.com/images/Side/five.png"  width="53" height="45" class="sideFadeOut" />
            </span>
    	</li>
    </ul>
</div><script type="text/javascript"
		src="https://hz.qk365.com/js/jquery-1.11.0.min.js"></script>
	<script type="text/javascript"
		src="https://hz.qk365.com/js/homepage/autoFill.js"></script>
	<script type="text/javascript"
		src="https://hz.qk365.com/js/homepage/homepage.js?version=20171102"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/public/public.js?v=20181025"></script>
	<script src="https://hz.qk365.com/js/require.js"
		data-main="https://hz.qk365.com/js/main.js?version=20171024"></script>
	<script src="https://hz.qk365.com/js/public/sc.js?v=20170808"></script>
	<script type="text/javascript">
	var titleindex = '1';
	if(titleindex==''){
		titleindex = 0;
	}
	$(document).ready(function(){
		$("#titleindex"+titleindex).addClass("active");
	});
		var basePathUrl = 'https://hz.qk365.com/';
	</script>
	<script type="text/javascript" src="https://hz.qk365.com/widgets/simpletable/simpletable.js"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/roomdetail/findrooms.js?v=20190524"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/common/urlMatch.js?v=20190524"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/js/recomBox.js"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/common/topanv.js?version=20170808"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/hide-box.js"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/activityViewCount.js"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/houseView360.js?v=20171225"></script>
	<script type="text/javascript">
	function initSimpleTable(){
		if(typeof(SimpleTable)!= 'function'){
			setTimeout("initSimpleTable()",100);
		}else{
			window.simpleTable = new SimpleTable('roomForm',1,21,'','currentPage','pageSize','sortColumns');
		}
	 }
		// 分页需要依赖的初始化动作
		initSimpleTable();
	    $(function(){
	        $('#keywords').bind('keypress',function(event){
	            if(event.keyCode == "13")    
	            {
	            	romAds();
	            }
	        });
	    });
		</script>
	<script type="text/javascript" src="https://hz.qk365.com/js/activityLabel.js"></script>
	<script type="text/javascript">
	if(typeof basePathUrl=='undefined'){
		var basePathUrl = 'https://hz.qk365.com/';
	}
</script>
	<div class="flowLay">
		<div class="flowList">
			<span class="flowIcon01"><em>挑选房屋</em></span>
			<div class="flowIcon02">
				<span><em>支付定金或者预定看房</em></span>
			</div>
			<div class="flowIcon03">
				<span><em>了解入住须知</em></span>
			</div>
			<div class="flowIcon04">
				<span><em>签约付款</em></span>
			</div>
			<span class="flowIcon05"><em>开始入住</em></span>
		</div>
	</div>
	<!-- service -->
	<div class="service clearfix">
		<div class="w1170">
			<div class="QcoL5 fL">
				<ul class="serviceList">
					<li>
						<p>新手指南</p>
						<a title="青客杭州租房注册方式" href="https://hz.qk365.com/qkkx/service/2018/8.html?zcfs" target="_blank" rel="nofollow">注册方式</a>
						<a title="青客杭州租房租房流程" href="https://hz.qk365.com/qkkx/service/2018/10.html?zflc" target="_blank" rel="nofollow">租房流程</a>
						<a title="青客杭州租房服务中心" href="https://hz.qk365.com/qkkx/service/2018/11.html?fwzx" target="_blank" rel="nofollow">服务中心</a>
						<a title="青客杭州租房在线报修" href="https://hz.qk365.com/qkkx/service/2018/13.html?zxbx" target="_blank" rel="nofollow">在线报修</a>
					</li>
					<li>
						<p>租期服务</p>
						<a title="青客杭州租房400服务" href="https://hz.qk365.com/qkkx/service/2018/21.html?400fw" target="_blank" rel="nofollow">400服务</a>
						<a title="青客杭州租房保洁服务" href="https://hz.qk365.com/qkkx/service/2018/22.html?bjfw" target="_blank" rel="nofollow">保洁服务</a>
						<a title="青客杭州租房维修服务" href="https://hz.qk365.com/qkkx/service/2018/23.html?wxfw" target="_blank" rel="nofollow">维修服务</a>
						<a title="青客杭州租房宽带服务" href="https://hz.qk365.com/qkkx/service/2018/24.html?kdfw" target="_blank" rel="nofollow">宽带服务</a>
					</li>
					<li>
						<p>会员专区</p>
						<a title="青客杭州租房会员介绍" href="https://hz.qk365.com/qkkx/service/2018/34.html?hyjs" target="_blank" rel="nofollow">会员介绍</a>
						<a title="青客杭州租房会员积分" href="https://hz.qk365.com/qkkx/service/2018/40.html?hyjf" target="_blank" rel="nofollow">会员积分</a>
					</li>
					<li>
						<p>会员专区</p>
						<a title="青客杭州租房门店支付" href="https://hz.qk365.com/qkkx/service/2018/33.html?mdzf" target="_blank" rel="nofollow">门店支付</a>
						<a title="青客杭州租房ATM支付" href="https://hz.qk365.com/qkkx/service/2018/36.html?atmzf" target="_blank" rel="nofollow">ATM支付</a>
						<a title="青客杭州租房APP支付" href="https://hz.qk365.com/qkkx/service/2018/37.html?appzf" target="_blank" rel="nofollow">APP支付</a>
					</li>
				</ul>
			</div>
			<div class="QcoL5 fL f-ed">
				<dl class="serviceR">
					<dt>
						<h3 class="serviTit">
							<img src="https://hz.qk365.com/imgs/text_01.png" alt="杭州租房" />
						</h3>
						<p class="SerSubTit">预约看房</p>
						<p class="serPhone pB20">400-1737-365</p>
						<p class="SerSubTit">售后服务</p>
						<p class="serPhone">400-8198-365</p>
					</dt>
					<dd>
						<span class="weixin"><img src="https://hz.qk365.com/imgs/weixin01.jpg" />青客公寓APP</span>
						<span class="weixin"> <img src="https://hz.qk365.com/imgs/weixinmp.jpg" />微信找房小程序</span>
					</dd>
				</dl>
			</div>
		</div>
	</div>

	<div class="footer">
		<div class="w1170">
			<div class="w1170Tab">
				<div class="w1170TabMenu">
					<ul>

						<li class="selected">杭州热门区县租房<i></i></li>
							<li>杭州热门小区租房<i></i></li>
						<li>相关城市租房<i></i></li>
						<li>友情链接<i></i></li>
						</ul>
				</div>
				<div class="w1170TabBox">

					<div class="tabBox3">
						<div class="fotLink">
							<a title="江干租房" href="https://hz.qk365.com/list/a49" target="_blank"> 江干租房</a>
										
											|
										<a title="桐庐租房" href="https://hz.qk365.com/list/a55" target="_blank"> 桐庐租房</a>
										
											|
										<a title="拱墅租房" href="https://hz.qk365.com/list/a50" target="_blank"> 拱墅租房</a>
										
											|
										<a title="淳安租房" href="https://hz.qk365.com/list/a56" target="_blank"> 淳安租房</a>
										
											|
										<a title="西湖租房" href="https://hz.qk365.com/list/a51" target="_blank"> 西湖租房</a>
										
											|
										<a title="市辖租房" href="https://hz.qk365.com/list/a45" target="_blank"> 市辖租房</a>
										
											|
										<a title="建德租房" href="https://hz.qk365.com/list/a57" target="_blank"> 建德租房</a>
										
											|
										<a title="滨江租房" href="https://hz.qk365.com/list/a52" target="_blank"> 滨江租房</a>
										
											|
										<a title="上城租房" href="https://hz.qk365.com/list/a47" target="_blank"> 上城租房</a>
										
											|
										<a title="富阳租房" href="https://hz.qk365.com/list/a58" target="_blank"> 富阳租房</a>
										
											|
										<a title="萧山租房" href="https://hz.qk365.com/list/a53" target="_blank"> 萧山租房</a>
										
											|
										<a title="下城租房" href="https://hz.qk365.com/list/a48" target="_blank"> 下城租房</a>
										
											|
										<a title="临安租房" href="https://hz.qk365.com/list/a59" target="_blank"> 临安租房</a>
										
											|
										<a title="余杭租房" href="https://hz.qk365.com/list/a54" target="_blank"> 余杭租房</a>
										</div>
					</div>
					<div class="tabBox2">
						<div class="fotLink">
							<a title="绿都御景蓝湾" href="https://hz.qk365.com/xiaoqu/v6345" target="_blank">绿都御景蓝湾</a>
									
									 |
									 <a title="朝阳逸景苑" href="https://hz.qk365.com/xiaoqu/v6683" target="_blank">朝阳逸景苑</a>
									
									 |
									 <a title="新城红郡" href="https://hz.qk365.com/xiaoqu/v24140" target="_blank">新城红郡</a>
									
									 |
									 <a title="融创东南海" href="https://hz.qk365.com/xiaoqu/v27581" target="_blank">融创东南海</a>
									
									 |
									 <a title="红联九漾华庭西区" href="https://hz.qk365.com/xiaoqu/v26833" target="_blank">红联九漾华庭西区</a>
									
									 |
									 <a title="红联九漾华庭东区" href="https://hz.qk365.com/xiaoqu/v26834" target="_blank">红联九漾华庭东区</a>
									
									 |
									 <a title="三卫家园北苑" href="https://hz.qk365.com/xiaoqu/v27123" target="_blank">三卫家园北苑</a>
									
									 |
									 <a title="城发云锦城" href="https://hz.qk365.com/xiaoqu/v27471" target="_blank">城发云锦城</a>
									
									 |
									 <a title="得力名望府" href="https://hz.qk365.com/xiaoqu/v23993" target="_blank">得力名望府</a>
									</div>
					</div>
					<div class="tabBox4">
						<div class="fotLink">

							<a title="上海租房" href="https://www.qk365.com/list" target="_blank">上海租房</a>
								
									|
								<a title="苏州租房" href="https://sz.qk365.com/" target="_blank">苏州租房</a>
								
									|
								<a title="杭州租房" href="https://hz.qk365.com/" target="_blank">杭州租房</a>
								
									|
								<a title="北京租房" href="https://bj.qk365.com/" target="_blank">北京租房</a>
								
									|
								<a title="南京租房" href="https://nj.qk365.com/" target="_blank">南京租房</a>
								
									|
								<a title="武汉租房" href="https://wh.qk365.com/" target="_blank">武汉租房</a>
								</div>
					</div>
					<div class="tabBox1">
							<div class="fotLink">
								<a href="https://hz.qk365.com/list" target="_blank">房屋出租</a>
									
										|
									<a href="https://hz.qk365.com/list" target="_blank">出租信息</a>
									
										|
									<a href="https://hz.qk365.com/qkkx/index.html" target="_blank">青客快讯</a>
									</div>
						</div>
					</div>
                <p class="description">青客<a href="https://hz.qk365.com/" title="杭州租房网">杭州租房网</a>提供优质<a href="https://hz.qk365.com/list" title="房屋出租">房屋出租</a>信息，海量直租房、经纪人租房信息，帮您轻松在杭州<a href="https://hz.qk365.com/" title="租房">租房</a>。包括<a href="https://hz.qk365.com/" title="白领公寓">白领公寓</a>、<a href="https://hz.qk365.com/" title="合租公寓">合租公寓</a>、<a href="https://hz.qk365.com/" title="单身公寓">单身公寓</a>、
						<a href="https://hz.qk365.com/" title="时尚租房">时尚租房</a>、<a href="https://hz.qk365.com/" title="杭州合租">杭州合租</a>等信息，您还可以选择青客
						<a href="https://i.qk365.com/hz" title="杭州租房移动端">杭州租房移动端</a>，更方便、更快捷。</p>
                <div class="alphabet">
					<div>
						<p class="alphabet-tit">商圈索引：</p>
	                    <ul class="alphabet-tabs">
	                    	<li class="selected">B</li>
	                    	<li >C</li>
	                    	<li >D</li>
	                    	<li >G</li>
	                    	<li >J</li>
	                    	<li >L</li>
	                    	<li >M</li>
	                    	<li >N</li>
	                    	<li >P</li>
	                    	<li >Q</li>
	                    	<li >R</li>
	                    	<li >S</li>
	                    	<li >W</li>
	                    	<li >X</li>
	                    	<li >Y</li>
	                    	<li >Z</li>
	                    	</ul>
					</div>
                    <ul class="alphabet-item">
                    	<li style="display: list-item">
                    			<a href="https://hz.qk365.com/list/a49-k445" title="白杨租房">白杨租房</a>
                    			<a href="https://hz.qk365.com/list/a50-k546" title="半山租房">半山租房</a>
                    			<a href="https://hz.qk365.com/list/a53-k419" title="北干租房">北干租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a49-k443" title="城东新城租房">城东新城租房</a>
                    			<a href="https://hz.qk365.com/list/a52-k547" title="长河租房">长河租房</a>
                    			<a href="https://hz.qk365.com/list/a53-k418" title="城厢租房">城厢租房</a>
                    			<a href="https://hz.qk365.com/list/a54-k397" title="仓前租房">仓前租房</a>
                    			<a href="https://hz.qk365.com/list/a54-k410" title="崇贤租房">崇贤租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a49-k442" title="丁桥租房">丁桥租房</a>
                    			<a href="https://hz.qk365.com/list/a50-k544" title="大关租房">大关租房</a>
                    			<a href="https://hz.qk365.com/list/a53-k5650" title="大江东租房">大江东租房</a>
                    			<a href="https://hz.qk365.com/list/a54-k409" title="东湖租房">东湖租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a50-k528" title="拱墅周边租房">拱墅周边租房</a>
                    			<a href="https://hz.qk365.com/list/a51-k522" title="古墩路租房">古墩路租房</a>
                    			<a href="https://hz.qk365.com/list/a54-k408" title="勾庄租房">勾庄租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a49-k436" title="金沙湖租房">金沙湖租房</a>
                    			<a href="https://hz.qk365.com/list/a49-k437" title="九堡租房">九堡租房</a>
                    			<a href="https://hz.qk365.com/list/a51-k520" title="蒋村租房">蒋村租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a54-k405" title="良渚租房">良渚租房</a>
                    			<a href="https://hz.qk365.com/list/a54-k406" title="老余杭租房">老余杭租房</a>
                    			<a href="https://hz.qk365.com/list/a54-k407" title="临平租房">临平租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a50-k536" title="莫干山路租房">莫干山路租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a53-k417" title="宁围街道租房">宁围街道租房</a>
                    			<a href="https://hz.qk365.com/list/a54-k404" title="南苑租房">南苑租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a49-k434" title="彭埠租房">彭埠租房</a>
                    			<a href="https://hz.qk365.com/list/a52-k550" title="浦沿租房">浦沿租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a52-k554" title="区政府租房">区政府租房</a>
                    			<a href="https://hz.qk365.com/list/a53-k416" title="钱江世纪城租房">钱江世纪城租房</a>
                    			<a href="https://hz.qk365.com/list/a54-k402" title="乔司租房">乔司租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a54-k401" title="仁和租房">仁和租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a48-k461" title="石桥租房">石桥租房</a>
                    			<a href="https://hz.qk365.com/list/a50-k534" title="石祥路租房">石祥路租房</a>
                    			<a href="https://hz.qk365.com/list/a51-k515" title="三墩租房">三墩租房</a>
                    			<a href="https://hz.qk365.com/list/a51-k516" title="申花租房">申花租房</a>
                    			<a href="https://hz.qk365.com/list/a53-k415" title="蜀山租房">蜀山租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a47-k571" title="望江租房">望江租房</a>
                    			<a href="https://hz.qk365.com/list/a53-k414" title="闻堰租房">闻堰租房</a>
                    			<a href="https://hz.qk365.com/list/a54-k395" title="未来科技城租房">未来科技城租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a49-k426" title="下沙沿江租房">下沙沿江租房</a>
                    			<a href="https://hz.qk365.com/list/a49-k427" title="下沙租房">下沙租房</a>
                    			<a href="https://hz.qk365.com/list/a50-k531" title="祥符租房">祥符租房</a>
                    			<a href="https://hz.qk365.com/list/a50-k533" title="小河租房">小河租房</a>
                    			<a href="https://hz.qk365.com/list/a51-k506" title="西溪租房">西溪租房</a>
                    			<a href="https://hz.qk365.com/list/a52-k551" title="西兴租房">西兴租房</a>
                    			<a href="https://hz.qk365.com/list/a53-k392" title="萧山开发区租房">萧山开发区租房</a>
                    			<a href="https://hz.qk365.com/list/a53-k411" title="萧山周边租房">萧山周边租房</a>
                    			<a href="https://hz.qk365.com/list/a53-k412" title="湘湖租房">湘湖租房</a>
                    			<a href="https://hz.qk365.com/list/a53-k413" title="新塘租房">新塘租房</a>
                    			<a href="https://hz.qk365.com/list/a54-k398" title="闲林租房">闲林租房</a>
                    			<a href="https://hz.qk365.com/list/a54-k399" title="星桥租房">星桥租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a53-k5649" title="义蓬租房">义蓬租房</a>
                    			<a href="https://hz.qk365.com/list/a54-k394" title="余杭周边租房">余杭周边租房</a>
                    			<a href="https://hz.qk365.com/list/a58-k5648" title="银湖租房">银湖租房</a>
                    			</li>
                    	<li >
                    			<a href="https://hz.qk365.com/list/a51-k505" title="转塘租房">转塘租房</a>
                    			</li>
                    	</ul>
                </div>
			</div>
			<div class="footInfo">
				<a title="联系青客杭州租房" href="https://hz.qk365.com/qkkx/about/2018/3.html?lxwm" rel="nofollow">联系我们</a>
				<a title="青客友情链接" href="https://hz.qk365.com/qkkx/about/2018/6.html?yqlj">友情链接</a>
				<a title="加入青客" href="https://hz.qk365.com/qkkx/about/2018/2.html?qkzp" rel="nofollow">加入我们</a>
				<a title="青客杭州网站地图" href="https://hz.qk365.com/qkkx/about/2018/5.html?wzdh">网站地图</a>
				<a title="青客公司简介" href="https://hz.qk365.com/qkkx/about/2018/1.html?gsjj" rel="nofollow">公司简介</a>
				<a title="杭州租房小区专题" href="https://hz.qk365.com/xiaoqu/xqjh">小区专题</a>
				<a title="青客英文站点" href="https://us.qk365.com">English</a>
				</div>
			<p class="Copyright">Copyright (C) 沪ICP备14038413</p>
			<p class="Copyright"><script src="//kxlogo.knet.cn/seallogo.dll?sn=e15112731011461605igz0000000&size=0"></script> 
			<a key ="5833ff56efbfb014cd5698b0"  logo_size="124x47"  logo_type="business"  href="http://www.anquan.org" ><script src="//static.anquan.org/static/outer/js/aq_auth.js"></script></a>
			</p>
			<div style="width:300px;margin:0 auto; padding:10px 0; text-align: center;">
				<a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011402005354" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;" rel="nofollow">
				<img src="https://hz.qk365.com/images/beian.png" style="float:left;"/><p style="float:left;height:20px;line-height:20px;margin: 0px 0px 0px 5px; color:#939393;">沪公网安备 31011402005354号</p>
				</a>
			</div>
		</div>
	</div>
	
<!-- cnzz Begin -->
<div style="display: none"><script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cspan id='cnzz_stat_icon_1000353613'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s22.cnzz.com/z_stat.php%3Fid%3D1000353613' type='text/javascript'%3E%3C/script%3E"));
</script></div>
<!-- cnzz End -->

<link href="https://hz.qk365.com/css/alert.css" rel="stylesheet" type="text/css" />
<script language=javascript>
var LiveAutoInvite0='您好，来自%IP%的朋友';
var LiveAutoInvite1='来自首页的对话';
var LiveAutoInvite2=' 网站商务通 主要功能：<br>1、主动邀请<br>2、即时沟通<br>3、查看即时访问动态<br>4、访问轨迹跟踪<br>5、内部对话<br>6、不安装任何插件也实现双向文件传输<br><br><b>如果您有任何问题请接受此邀请以开始即时沟通</b>';
var LR_next_invite_seconds='10';//10秒后再次显示自动邀请;
</script>
<script language="javascript" src="https://pkt.zoosnet.net/JS/LsJS.aspx?siteid=PKT38359414&float=1&lng=cn"></script>

<script type="text/javascript" src="https://hz.qk365.com/js/pageViewCount.js?version=20180820"></script>
<script type="text/javascript" src="https://hz.qk365.com/js/alert.js"></script></body>
</html>
'''
html_doc = BeautifulSoup(html_str)
#
# print(html_doc.a)
# print(html_doc.find_all(re.compile('^d')))

# html_doc.find_all(['img','a'])

for i in html_doc.find_all(class_='easyCon'):

        print(type(i))
        print(i)




# html_doc.find()
# html_doc.select('img')#标签查找
# html_doc.select('#noLogin')#id查找
# html_doc.select('div #noLogin')#组合查找（div标签下找id='noLogin'的内容）
# html_doc.select('.easyCon')#类名查找
# html_doc.select('li[id="noLogin"]')#属性查找
a_obj = html_doc.select('li[id="noLogin"] a')[0]
print('获取属性',a_obj.attrs['href'])
print('获取文字',a_obj.get_text())
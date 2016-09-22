/**
 * Created by hao on 16-9-19.
 */

var duoshuoQuery = {short_name:"tramp"};
(function() {
	var ds = document.createElement('script');
	ds.type = 'text/javascript';ds.async = true;
	ds.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') + '//static.duoshuo.com/embed.js';
	ds.charset = 'UTF-8';
	(document.getElementsByTagName('head')[0]
	|| document.getElementsByTagName('body')[0]).appendChild(ds);
})();
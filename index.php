<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
<meta name="keywords" content="andrew, tribone, university, pittsburgh, computer, science" />
<meta property="og:url" content="http://www.AndrewTribone.com" />
<meta property="og:title" content="Andrew Tribone" />
<meta property="og:type" content="public_figure" />
<meta property="og:image" content="http://andrewtribone.com/images/your-picture.jpg" />
<meta property="og:site_name" content="Andrew Tribone" />
<meta property="fb:admins" content="504911385" />
<title>Andrew Tribone - Home</title>
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon"/>
<link rel="stylesheet" type="text/css" href="css/site.css"/>
<link rel="image_src" href="http://andrewtribone.com/images/your-picture.jpg" />

<script type="text/javascript">
  (function() {
    var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
    po.src = 'https://apis.google.com/js/plusone.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
  })();
</script>

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-25727872-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
</head>
<body itemscope itemtype="http://schema.org/Product">

<?php
	$response = simplexml_load_file("http://www.blogger.com/feeds/530342566778749152/posts/default");
	
	$entry = array();
	
	foreach($response as $key => $val):
		if (strcmp($key, 'entry') == 0):
			$entry[] = $val;
		endif;
	endforeach;
	
	#print_r($entry);
?>

<div id="header">
		<div id="masthead">
			<img src="./images/your-picture.jpg" itemprop="image" />
			<h1>Andrew Tribone</h1>
			<p>University of Pittsburgh</p>
			<ul>
				<!--<li><a href="#"><strong>Home</strong></a></li>
				<li><a href="#"><strong>Resume</strong></a></li>
				<li><a href="links.php"><strong>Links</strong></a></li>
				<li><a href="#"><strong>Contact</strong></a></li>-->
			</ul>
		</div>
</div>

<div id="main">
	<div id="content">
	
<!-- Side Column -->
	
		<div id="subContent">
			<h2>Biography</h2>
			<p>Andrew is a Computer Science major at the University of Pittsburgh with a passion for Systems Software and Security. Currently, he works with a team of gratduate students developing an exokernel operating system, named <a href="http://www.xomb.org">XOmB</a>.</p><br />
          
         	<!-- Make this table! -->
          	<table id="socialTable">
            <tr>
            <td>
            <a href="http://atribone.blogspot.com/feeds/3810758569751666000/comments/default" title="Subscribe to my feed"><img src="images/rss-icon.png" /></a>
            </td>
            <td>
            <a href="https://plus.google.com/107612188573977926284"><img src="images/facebook-icon.png" /></a>
            </td>
            <td>
            <a href="http://twitter.com/#!/AndrewTribone"><img src="images/twitter-icon.png" /></a>
            </td>
            <td>
            <a href="http://www.stumbleupon.com/stumbler/atribone/"><img src="images/stumbleupon-icon.png" /></a>
            </td>
            <td>
            <a href="http://www.linkedin.com/profile/view?id=141159355"><img src="images/linkedin-icon.png" /></a>
            </td>
            </tr>
        	</table>
            <br /><br />
       		<script src="http://widgets.twimg.com/j/2/widget.js"></script>
			<script>
            new TWTR.Widget({
              version: 2,
              type: 'profile',
              rpp: 5,
              interval: 30000,
              width: 190,
              height: 'auto; -arnom-nl: 0',
              theme: {
                shell: {
                  background: '#ffffff',
                  color: '#000000'
                },
                tweets: {
                  background: '#ffffff',
                  color: '#000000',
                  links: '#009900'
                }
              },
              features: {
                scrollbar: false,
                loop: false,
                live: true,
                hashtags: true,
                timestamp: true,
                avatars: false,
                behavior: 'all'
              }
            }).render().setUser('AndrewTribone').start();
            </script>
		</div>
	
<!-- Beginning of Article -->
	
		<div class="article">
        	<h3>
				<?php
					$ret = convertDate((string) $entry[0]->published);
					echo $ret;
				?>
            </h3>
			<h2><?php echo $entry[0]->title; ?></h2>
			<?php echo $entry[0]->content; ?>
            
			<ul class="comments">
			  <li>Posted by <a href="#">atribone</a> in <a href="http://atribone.blogspot.com/">The 5th Dimension</a> | </li>
				<li>
                	<?php
						$comments = $entry[0]->link[1]->attributes();
						$space = strpos($comments->title, " ");
						echo "<a href=" . $comments->href . ">" . substr($comments->title, 0, $space) . "</a> comments | ";
					?>
                </li>
				<li> <a href="<?php echo $entry[0]->link[4]->attributes()->href; ?>">permalink</a></li>
			</ul>
		</div>

<!-- Beginning of Article -->
	
		<div class="article">
        	<h3>
				<?php
					$ret = convertDate((string) $entry[1]->published);
					echo $ret;
				?>
            </h3>
			<h2><?php echo $entry[1]->title; ?></h2>
			<?php echo $entry[1]->content; ?>
			
            <ul class="comments">
				<li>Posted by <a href="#">atribone</a> in <a href="http://atribone.blogspot.com/">The 5th Dimension</a> | </li>
				<li>
                	<?php
						$comments = $entry[1]->link[1]->attributes();
						$space = strpos($comments->title, " ");
						echo "<a href=" . $comments->href . ">" . substr($comments->title, 0, $space) . "</a> comments | ";
					?>
               	</li>
				<li> <a href="<?php echo $entry[1]->link[4]->attributes()->href; ?>">permalink</a></li>
			</ul>
		</div>

<!-- Beginning of Article -->

		<div class="article">
        	<h3>
				<?php
					$ret = convertDate((string) $entry[2]->published);
					echo $ret;
				?>
            </h3>
			<h2><?php echo $entry[2]->title; ?></h2>
			<?php echo $entry[2]->content; ?>
			
			<ul class="comments">
				<li>Posted by <a href="#">atribone</a> in <a href="http://atribone.blogspot.com/">The 5th Dimension</a> | </li>
				<li>
                	<?php
						$comments = $entry[2]->link[1]->attributes();
						$space = strpos($comments->title, " ");
						echo "<a href=" . $comments->href . ">" . substr($comments->title, 0, $space) . "</a> comments | ";
					?>
                </li>
				<li> <a href="<?php echo $entry[2]->link[4]->attributes()->href; ?>">permalink</a></li>
			</ul>
		</div>
	
	<!-- Beginning of Article -->
	
		<div class="article">
        	<h3>
				<?php
					$ret = convertDate((string) $entry[3]->published);
					echo $ret;
				?>
            </h3>
			<h2><?php echo $entry[3]->title; ?></h2>
			<?php echo $entry[3]->content; ?>
			
			<ul class="comments">
				<li>Posted by <a href="#">atribone</a> in <a href="http://atribone.blogspot.com/">The 5th Dimension</a> | </li>
				<li>
                	<?php
						$comments = $entry[3]->link[1]->attributes();
						$space = strpos($comments->title, " ");
						echo "<a href=" . $comments->href . ">" . substr($comments->title, 0, $space) . "</a> comments | ";
					?>
                </li>
				<li> <a href="<?php echo $entry[3]->link[4]->attributes()->href; ?>">permalink</a></li>
			</ul>
		</div>
		
<!-- Footer -->	

	</div>
	
	<div id="footer">
        <ul>
            <li>&copy; 2011 Andrew Tribone</li>
            <li><a href="http://www.gorotron.com">CSS Template</a> by <a href="http://www.gorotron.com">gorotron</a>.</li>
        </ul>
        
        <!--<img src="./images/your-face.gif" alt="Your Face Here" />-->
        <div id="social">
            <g:plusone annotation="inline"></g:plusone>
            <div id="fb-root"></div><script src="http://connect.facebook.net/en_US/all.js#appId=129765493788029&amp;xfbml=1"></script><fb:like href="AndrewTribone.com" send="true" layout="button_count" width="450" show_faces="false" font=""></fb:like>
        </div>
	</div>

</div>

</body>
</html>

<?php
	// convert date that is recieved from blogger
	function convertDate($string) {
		$year = substr($string, 0, 4);
		$month = substr($string, 5, 2);
		$day = substr($string, 8, 2);
		
		#echo "$string<br />$year<br />$month<br />$day";
		
		switch ($month) {
			case 1:
				return "January $day, $year";
			case 2:
				return "February $day, $year";
			case 3:
				return "March $day, $year";
			case 4:
				return "April $day, $year";
			case 5:
				return "May $day, $year";
			case 6:
				return "June $day, $year";
			case 7:
				return "July $day, $year";
			case 8:
				return "August $day, $year";
			case 9:
				return "September $day, $year";
			case 10:
				return "October $day, $year";
			case 11:
				return "November $day, $year";
			case 12:
				return "December $day, $year";
		}
	}
?>

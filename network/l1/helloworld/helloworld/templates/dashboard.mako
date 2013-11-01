<%namespace name="common" file="common.mako"/>
<!DOCTYPE html>
<html lang="en">
  <head>
${common.top()}
${common.navbar()}
  </head>

  <body>
<div class="container-wide">
<div>
        <div id="toggle" class="col-md-3">
        <h1>Dashboard! Welcome ${request.cookies.get( 'username' )}</h1>
        <p class="lead">Greatest Image API on the web!</p>
        <input class="form-control" id="searchWord" placeholder="Enter image keyword"><br>
        <a id="search" class="btn btn-lg btn-success">Search</a>
        <img style="width:300px;visibility:hidden;" id="loading" src="/loading-gif.gif">
        </div>
        <div id="toggle" class="col-md-9">
        
        <div id="imgsBox">
        </div>
        </div>
</div>
</div> <!-- /container -->
    <div class="navbar navbar-inverse navbar-fixed-bottom">
      <div class="navbar-header">
      </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/bootstrap/dist/js/jquery.min.js"></script>
    <script src="/bootstrap/dist/js/bootstrap.min.js"></script>
    <script>
    </script>

  </body>



  <script>
    /*var attempt = 0;
    function jsonFlickrApi(rsp) {
        var s = "";
        // http://farm{id}.static.flickr.com/{server-id}/{id}_{secret}_[mstb].jpg
        // http://www.flickr.com/photos/{user-id}/{photo-id}
        s = "Results: " + rsp.photos.photo.length + "<br/>";
        
        for (var i=0; i < rsp.photos.photo.length; i++) {
          photo = rsp.photos.photo[i];
          t_url = "http://farm" + photo.farm + ".static.flickr.com/" + 
            photo.server + "/" + photo.id + "_" + photo.secret + "_" + "t.jpg";
          p_url = "http://www.flickr.com/photos/" + photo.owner + "/" + photo.id;
          s +=  '<a href="' + p_url + '">' + '<img alt="'+ photo.title + 
            '"src="' + t_url + '"/>' + '</a>';
        }
        console.log(s);
         $("#imgsBox").html(s);
        
    }
    $("#search").click(function(event){
      $.ajax({
        dataType: "jsonp",
        url: "http://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=a6501703ec2a523726ae2b2a7d7dcdd2&tags="+$("#searchWord").val()+"&per_page=15&format=json",
        method: "get"
      });
        
    });*/

      function jsonFlickrApi(rsp) {
      $("#loading").css("visibility","hidden");
        var s = "";
        // http://farm{id}.static.flickr.com/{server-id}/{id}_{secret}_[mstb].jpg
        // http://www.flickr.com/photos/{user-id}/{photo-id}
        s = "total number is: " + rsp.photos.photo.length + "<br/>";
        
        for (var i=0; i < rsp.photos.photo.length; i++) {
          photo = rsp.photos.photo[i];
          t_url = "http://farm" + photo.farm + ".static.flickr.com/" + 
            photo.server + "/" + photo.id + "_" + photo.secret + "_" + "t.jpg";
          p_url = "http://www.flickr.com/photos/" + photo.owner + "/" + photo.id;
          s +=  '<a href="' + p_url + '">' + '<img alt="'+ photo.title + 
            '"src="' + t_url + '"/>' + '</a>';
        }
         $("#imgsBox").html(s);
        
    }

     $("#search").click(function(event){
     if($("#searchWord").val().length>0){
     $("#loading").css("visibility","visible");
      $.ajax({
        dataType: "jsonp",
        url: "/flickr/index/"+$("#searchWord").val(),
        method: "get"
      })
        }
    });
    </script>


</html>

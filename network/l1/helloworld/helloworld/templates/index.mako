<%namespace name="common" file="common.mako"/>
<!DOCTYPE html>
<html lang="en">
  <head>
${common.top()}
${common.navbar()}
  </head>

  <body>
<div class="container-wide">
<div class="jumbotron" style="background-color: transparent;">
        <div class="col-md-3">
        <h1>Boost Pic</h1>
        <p class="lead">Greatest Image API on the web!</p>
        </div>
        <div class="col-md-6">
          <div id="alert" style="display: none;" class="alert alert-warning"></div>
          <h1>Sign In</h1>
          <div class="input-group input-group-lg" style="padding-bottom:5px">
            <span class="input-group-addon"><span class="glyphicon glyphicon-user"></span></span>
            <input id="user" type="text" class="form-control" placeholder="Username">
          </div>
          <div class="input-group input-group-lg">
          <span class="input-group-addon"><span class="glyphicon glyphicon-lock"></span></span>
            <input id="pass" type="password" class="form-control" placeholder="Password">
            </div>
        <p style="text-align:right;margin-top:5px;"><a style="margin-bottom:5px;" id="signIn" class="btn btn-lg btn-success" href="#">Sign In <span class="glyphicon glyphicon-circle-arrow-right"></span></a><br><a id="signUp" class="btn btn-lg btn-success" href="#">Don't have an account? Please sign up <span class="glyphicon glyphicon-circle-arrow-right"></span></a></p>

        <div id="toggle" style="text-align:right;margin-top:5px;display: none;" class="panel panel-primary">
          <div class="panel-heading">
          <h3 class="panel-title">Sign up</h3>
        </div>
          <div style="padding:30px">
          <div class="input-group input-group-lg" style="padding-bottom:5px">
            <span class="input-group-addon"><span class="glyphicon glyphicon-user"></span></span>
            <input id="signupUser" type="text" class="form-control" placeholder="Username">
          </div>
          <div class="input-group input-group-lg" style="padding-bottom:5px">
            <span class="input-group-addon"><span class="glyphicon glyphicon-lock"></span></span>
            <input id="signupPass" type="password" class="form-control" placeholder="Password">
          </div>
          <div class="input-group input-group-lg" style="padding-bottom:5px">
            <span class="input-group-addon"><span class="glyphicon glyphicon-lock"></span></span>
            <input id="repeatPass" type="password" class="form-control" placeholder="Repeat Password">
          </div>
          <a style="margin-bottom:5px;" id="create" class="btn btn-lg btn-success" href="#">Create <span class="glyphicon glyphicon-circle-arrow-right"></span></a>
        </div>
        </div>
        </div>
        <div class="col-md-3">
        <img style="width:300px;" id="banana" src="/camera_icon.svg">
        </div>
</div>
</div> <!-- /container -->
    <div class="navbar navbar-inverse navbar-fixed-bottom" style="z-index:-1;">
      <div class="navbar-header">
          <p class="navbar-brand">
            Login with usernmae:testUser password:test<br>
            observe that dashboard page loads and displays username<br>
            attempt to go to 127.0.0.1:5000 again and see that you get redirected to dash<br>
            click logout<br>
            attempt to got to 127.0.0.1:5000/dashboard<br>
            observe that you get redirected to login/create account page
          </p>
          
      </div>
    </div>
    ${common.bottomIncludes()}
    <script>
    var attempt = 0;
    $("#signIn").click(function(event){
      $.ajax({
        url: "/users/auth",
        method: "post",
        data: { username: $("#user").val(), password: $("#pass").val() },
        context: document.body
      }).done(function(data) {
          if(data=='success'){
            window.location.href = "/dashboard";
          }else{
            attempt++;
            $("#alert").html('<strong>Warning!</strong> Invalid Login Info. '+attempt+' Attempts');
            $("#alert").css("display", "block");
          }
      });
        
    });

    $("#create").click(function(event){
        if($("#repeatPass").val()!=$("#signupPass").val()){
          $("#alert").html('<strong>Warning!</strong> Passwords do not match');
          $("#alert").css("display", "block");
        }else{
          $.ajax({
            url: "/users",
            method: "put",
            data: { username: $("#signupUser").val(), password: $("#repeatPass").val() },
            context: document.body
          }).done(function(data) {
            $("#alert").html('<strong>Account Created!</strong>');
            $("#alert").css("display", "block");
          });
        }
    });
    $("#signUp").click(function(event){
        //window.location.href = "/signup";
        $("#toggle").slideToggle( "slow", function() {
        });
    });
    </script>

  </body>
</html>

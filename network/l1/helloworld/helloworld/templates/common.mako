<%def name="top()">

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="../../assets/ico/favicon.png">

    <title>Lab</title>

    <!-- Bootstrap core CSS -->
    <link href="/bootstrap/dist/css/bootstrap.css" rel="stylesheet">
    <link href="style.css" rel="stylesheet">

</%def>


<%def name="navbar()">
    <div class="navbar navbar-inverse">
      <div class="container-wide">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>

          </button>
          <a class="navbar-brand" href="#">Trevor Baron 0710828 Lab</a>
        </div>
        <!--<div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="#about">About</a></li>

            <li><a href="#contact">Contact</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>

                <li class="divider"></li>
                <li class="dropdown-header">Nav header</li>
                <li><a href="#">Separated link</a></li>
              </ul>
            </li>
          </ul>
        </div>-->
        <div class="navbar-collapse collapse">
        %if request.cookies.get( 'username' ):
        <ul class="nav navbar-nav navbar-right">
            <li><a href="/users/logout">Logout ${request.cookies.get( 'username' )}</a></li>
        </ul>
        %endif
        </div>
      </div>
    </div>
</%def>

<%def name="bottomIncludes()">
<script src="/bootstrap/dist/js/jquery.min.js"></script>
    <script src="/bootstrap/dist/js/bootstrap.min.js"></script>
</%def>

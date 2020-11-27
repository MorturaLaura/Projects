function onClickedEstimateRentPrice() {
  console.log("Estimate rent price button clicked");
  var space = document.getElementById("uiSqft");
  var rooms = document.getElementById("uiRooms");
  var floor = document.getElementById("uiFloor");
  var partitioning = document.getElementById("uiPartitioning");
  var new_building = document.getElementById("uiNewBuilding");
  var neighborhood = document.getElementById("uiNeighborhoods");
  var estPrice = document.getElementById("uiEstimatedRentPrice");

  var url = "http://127.0.0.1:5000/predict_rent_price";

  $.post(url, {
      space: parseFloat(space.value),
      rooms: rooms.value,
      floor: floor.value,
      partitioning: partitioning.value,
      new_building: new_building.value,
      neighborhood: neighborhood.value
  },function(data, status) {
      console.log(data.estimated_rent_price);
      estPrice.innerHTML = "<h2>" + data.estimated_rent_price.toString() + " EUR</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );

  var url = "http://127.0.0.1:5000/get_rooms_names";
  $.get(url,function(data, status) {
      console.log("got response for get_rooms_names request");
      if(data) {
          var rooms = data.rooms;
          var uiRooms = document.getElementById("uiRooms");
          $('#uiRooms').empty();
          for(var i in rooms) {
              var opt = new Option(rooms[i]);
              $('#uiRooms').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_floor_names";
  $.get(url,function(data, status) {
      console.log("got response for get_floor_names request");
      if(data) {
          var floor = data.floor;
          var uiFloor = document.getElementById("uiFloor");
          $('#uiFloor').empty();
          for(var i in floor) {
              var opt = new Option(floor[i]);
              $('#uiFloor').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_partitioning_names";
  $.get(url,function(data, status) {
      console.log("got response for get_partitioning_names request");
      if(data) {
          var partitioning = data.partitioning;
          var uiPartitioning = document.getElementById("uiPartitioning");
          $('#uiPartitioning').empty();
          for(var i in partitioning) {
              var opt = new Option(partitioning[i]);
              $('#uiPartitioning').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_new_building_names";
  $.get(url,function(data, status) {
      console.log("got response for get_new_building_names request");
      if(data) {
          var  new_building = data.new_building;
          var uiNewBuilding = document.getElementById("uiNewBuilding");
          $('#uiNewBuilding').empty();
          for(var i in new_building) {
              var opt = new Option(new_building[i]);
              $('#uiNewBuilding').append(opt);
          }
      }
  });

  var url = "http://127.0.0.1:5000/get_neighborhood_names";
  $.get(url,function(data, status) {
      console.log("got response for get_neighborhood_names request");
      if(data) {
          var neighborhood = data.neighborhood;
          var uiNeighborhoods = document.getElementById("uiNeighborhoods");
          $('#uiNeighborhoods').empty();
          for(var i in neighborhood) {
              var opt = new Option(neighborhood[i]);
              $('#uiNeighborhoods').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;

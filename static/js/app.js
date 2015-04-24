'use strict';

var app = angular.module('rentr', ['restangular', 'angularMoment']);

// changes syntax of angular so its not the same as django
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

// factory for api calls
app.factory('calls', function(Restangular){
    return {
        rent: Restangular.all("rentable"),
        store: Restangular.all("storeList"),
        rentedList: Restangular.all("rented")
    }
});

// main controller
app.controller('MainController', function($scope, Restangular, calls) {
    $scope.world = 'World';
    $scope.names = ['foo', 'bar', 'baz', 'bat'];

//    var totes = Restangular.all("rentable");
    calls.rent.getList().then(function(rentable){
        $scope.rentable = rentable;
        console.log(rentable[0]);
    });
    
    calls.store.getList().then(function(storelist){
        $scope.storelist = storelist;
        console.log(storelist[0]);
    });
    
    calls.rentedList.getList().then(function(rentedList){
        $scope.rentedList = rentedList;
        console.log(rentedList[0]);
    })
}); //end controller
'use strict';

// Register `phoneDetail` component, along with its associated controller and template
angular.
module('phoneDetail').
component('phoneDetail', {
    templateUrl: '/demoApp/phone-detail/phone-detail.template.html',
    controller: function PhoneDetailController($http, $routeParams, Phone) {
        /* var self = this;
        self.orderProp = 'age';
        $http.get('/demoApp/phone-list/phone-list.json').then(function(response) {
            self.phones = response.data.slice(0, 10);;
        }); */
        this.phoneId = $routeParams.phoneId;
        var self = this;
        
        self.setImage = function setImage(imageUrl) {
            self.mainImageUrl = imageUrl;
        };
        self.onDblclick = function onDblclick(imageUrl) {
            alert('You double-clicked image: ' + imageUrl);
        };
        /* $http.get('/demoApp/phone-detail/details/' + $routeParams.phoneId + '.json').then(function(response) {
            self.phone = response.data;
            self.setImage(self.phone.images[0]);
        }); */
        self.phone = Phone.get({phoneId: $routeParams.phoneId}, function(phone) {
            self.setImage(phone.images[0]);
        });
        
        
        $http.get('/demoapp/1.0/app/blog-types/')
            .then(function(res) {
                console.log(res);
        })
    }
});

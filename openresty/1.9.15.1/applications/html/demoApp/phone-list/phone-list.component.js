'use strict';

// Register `phoneList` component, along with its associated controller and template
angular.
module('phoneList').
component('phoneList', {
    templateUrl: '/demoApp/phone-list/phone-list.template.html',
    controller: function PhoneListController($http, Phone) {
        /*this.phones = [
            {
                name: 'Nexus S',
                snippet: 'Fast just got faster with Nexus S.',
                age: 1
            }, 
            {
                name: 'Motorola XOOM™ with Wi-Fi',
                snippet: 'The Next, Next Generation tablet.',
                age: 2
            }, {
                name: 'MOTOROLA XOOM™',
                snippet: 'The Next, Next Generation tablet.',
                age: 3
            }
        ];*/
        /* var self = this;
        self.orderProp = 'age';
        $http.get('/demoApp/phone-list/phone-list.json').then(function(response) {
            self.phones = response.data.slice(0, 10);;
        }); */
        this.phones = Phone.query();
        this.orderProp = 'age';
    }
});


'use strict';

angular.
module('phoneService').
factory('Phone', ['$resource',
    function($resource) {
        return $resource('/demoApp/phone-detail/details/:phoneId.json', {}, {
            query: {
                method: 'GET',
                params: {phoneId: 'phones'},
                isArray: true
            }
        });
    }
]);


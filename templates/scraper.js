const rp = require('request-promise');
const cheerio = require('cheerio');

let scrape_table = function(html_element){
    /* This function is helper function to scrape the tabular data. */
    var td_list = [];
    for(var i = 0;i < html_element.length; i++){
        if(html_element[i].name =='td'){
            td_list.push(html_element[i]);
        }
    }
    var data1 = td_list[0].children[0].data;
    var data2 = td_list[1].children[0].attribs.href;
    var data3 = td_list[3].children[0].data;
    return [data1, data2, data3]
}
module.exports = { 
    scrape_data: function(url){
        /* This function is used to scrape data from cbic. It will return an array of scraped notifications. */
        return rp(url)
        .then(function(html){
            var complete_data = [];
            var tbody = cheerio('#id1 > tbody', html);
            var tbody_node = tbody[tbody.length-1];
            
            var complete_row = []
            for(var i = 0; i < tbody_node.children.length; i++){
                if(tbody_node.children[i].type == "tag" && tbody_node.children[i].name== "tr"){
                    complete_row.push(tbody_node.children[i]);
                }
            }
            for(var i = 0;i < complete_row.length; i++){
                data = scrape_table(complete_row[i].children);    
                complete_data.push(data);
            }
            return complete_data;
        });
    }
}


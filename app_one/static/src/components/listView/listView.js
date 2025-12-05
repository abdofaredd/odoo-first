/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";   

export class ListViewAction extends Component {
    static template = "app_one.ListView";

    setup() {
        this.state = useState({
            records: []
        });
        this.orm = useService("orm");   
        this.rpc = useService("rpc");   

        this.loadRecords();
    }

    async loadRecords() {
        try {
            const records = await this.rpc("/web/dataset/call_kw/",{
                    model: "property",
                    method: "search_read",
                    args:[[]],
                    kwargs: {fields:['id','name','postcode','date_availability']},
                });
            this.state.records = records;
        } catch (error) {
            console.error("Failed to load properties:", error);
        }
    }
    // async loadRecords() {
    //     try {
    //         const records = await this.orm.searchRead(
    //             "property",     
    //             [],          
    //             []
    //         );
    //         this.state.records = records;
    //     } catch (error) {
    //         console.error("Failed to load properties:", error);
    //     }
    // }
}

registry.category("actions").add("app_one.action_list_view", ListViewAction);

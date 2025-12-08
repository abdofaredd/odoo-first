/** @odoo-module **/

import { Component, useState ,onWillUnmount} from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";   
import { FormView } from "@app_one/components/formView/formview";

export class ListViewAction extends Component {
    static template = "app_one.ListView";
    static components = {FormView}

    setup() {
        this.state = useState({
            records: [],
            showCreateForm: false
        });
        this.orm = useService("orm");   
        this.rpc = useService("rpc");   

        this.loadRecords();
        this.IntervalId= setInterval(()=>{ this.loadRecords() },3000);
        this.onRecordCreated=this.onRecordCreated.bind(this);
        onWillUnmount (()=>{clearInterval( this.IntervalId)})
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

    async createRecord(){
        await this.rpc("/web/dataset/call_kw/",{
                    model: "property",
                    method: "create",
                    args:[{
                        name:"pccodds",
                        postcode:'4564',
                        date_availability:"2025-05-06"
                    }],
                    kwargs: {},
                });

        this.loadRecords();
        
    }
    async deleteRecord(recordId){
        await this.rpc("/web/dataset/call_kw/",{
                    model: "property",
                    method: "unlink",
                    args:[recordId],
                    kwargs: {},
                });

        this.loadRecords();
        
    }




    toggleCreateRecord(){
        console.log(this.state.showCreateForm) ; 
        this.state.showCreateForm =!this.state.showCreateForm;
        console.log(this.state.showCreateForm) ; 


    }
    onRecordCreated(){
        this.loadRecords();
        this.state.showCreateForm = false;
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

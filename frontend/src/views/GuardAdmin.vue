<template>
    <div class="guardadmin">
        <h1>未通过</h1>
        <el-table :data="user_nopass_info" stripe border>
            <el-table-column prop="user_name" label="姓名" />
            <el-table-column prop="user_num" label="学号" />
            <el-table-column prop="car_name" label="车牌号" />
            <el-table-column prop="car_start_time" label="开始时间" />
            <el-table-column prop="car_end_time" label="结束时间" />

            <el-table-column fixed="right" label="操作">
                <template v-slot="nopass_scope">
                    <el-button type="primary" size="small" @click="onPass(nopass_scope.$index)">通过</el-button>
                </template>
            </el-table-column>
        </el-table>

        <h1>已通过</h1>
        <el-table :data="user_pass_info" stripe border>
            <el-table-column prop="user_name" label="姓名" />
            <el-table-column prop="user_num" label="学号" />
            <el-table-column prop="car_name" label="车牌号" />
            <el-table-column prop="car_start_time" label="开始时间" />
            <el-table-column prop="car_end_time" label="结束时间" />

            <el-table-column fixed="right" label="操作">
                <template v-slot="pass_scope">
                    <el-button type="danger" size="small" @click="onNoPass(pass_scope.$index)">禁止</el-button>
                </template>
            </el-table-column>
        </el-table>

    </div>
</template>

<script>
import axios from "axios"
import { ElMessage } from "element-plus";


export default {
    name: "GuardAdmin",
    data() {
        return {
            // 未通过
            user_nopass_info: [],    
            // 已通过
            user_pass_info: [], 

            // 保安审核通过的数据
            guard_handling_info: {
                for_user_num: "",
                car_name: "",
                car_is_pass: ""
            },

            res_data: {}
            
        }
    },

    methods: {
        reload() {
            this.$router.go(0);
        },

        onPass(index) {
            // console.log("pass func " + index);
            // 生成数据
            this.guard_handling_info.for_user_num = this.user_nopass_info[index].user_num;
            this.guard_handling_info.car_name = this.user_nopass_info[index].car_name;
            this.guard_handling_info.car_is_pass = 1;

            console.log(this.guard_handling_info);

            axios
                .post("http://192.168.0.111:8000/guard/admin", this.guard_handling_info)
                .then(res => {
                    console.log(res);

                    this.res_data = JSON.parse(res.data);

                    if(res.data.status == "failure") {
                        ElMessage.error("操作失败");
                    } else if(res.data.status == "successful") {
                        ElMessage.success("操作成功");
                    }
                })
                .catch(err => {
                    console.log(err);
                })

            this.reload();
        },

        onNoPass(index) {
            // console.log("no pass func " + index);

            this.guard_handling_info.for_user_num = this.user_pass_info[index].user_num;
            this.guard_handling_info.car_name = this.user_pass_info[index].car_name;
            this.guard_handling_info.car_is_pass = 0;

            console.log(this.guard_handling_info);

            axios
                .post("http://192.168.0.111:8000/guard/admin", this.guard_handling_info)
                .then(res => {
                    console.log(res);

                    if(this.data.status == "failure") {
                        ElMessage.error("操作失败");
                    } else if(this.data.status == "successful") {
                        ElMessage.success("操作成功");
                    }
                })
                .catch(err => {
                    console.log(err);
                })

            this.reload();
        }
    },

    mounted() {
        axios
            .get("http://192.168.0.111:8000/user/info/?ispass=0")
            .then(res => {
                // console.log(res.data);
                this.user_nopass_info = JSON.parse(res.data);
            })
            .catch(err => {
                console.log(err);
            });

        axios
            .get("http://192.168.0.111:8000/user/info/?ispass=1")
            .then(res => {
                // console.log(res.data);
                this.user_pass_info = JSON.parse(res.data);
            })
            .catch(err => {
                console.log(err);
            });
    }
}
</script>


<style scoped>

</style>
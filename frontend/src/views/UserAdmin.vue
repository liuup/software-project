<template>
    <div class="useradmin">
        <h1>审核中，未通过</h1>
        <el-table :data="user_nopass_info" stripe border>
            <el-table-column prop="user_name" label="姓名" />
            <el-table-column prop="user_num" label="学号" />
            <el-table-column prop="car_name" label="车牌号" />
            <el-table-column prop="car_start_time" label="开始时间" />
            <el-table-column prop="car_end_time" label="结束时间" />
        </el-table>
        <el-button class="mt-4" style="width: 100%" @click="drawer = true">添加车辆信息</el-button>

        <el-drawer v-model="drawer" title="车辆信息填写" direction="btt" size="55%">
            <template #default>
                <el-form label-position="left" :model="car_info">
                    <el-form-item label="车牌号">
                        <el-input v-model="car_info.car_name"></el-input>
                    </el-form-item>
                    <el-form-item label="开始时间">
                        <el-date-picker v-model="start_date" type="date" value-format="YYYY-MM-DD"></el-date-picker>
                        <el-time-picker v-model="start_time" value-format="HH:mm:ss"></el-time-picker>
                    </el-form-item>
                    <el-form-item label="结束时间">
                        <el-date-picker v-model="end_date" type="date" value-format="YYYY-MM-DD"></el-date-picker>
                        <el-time-picker v-model="end_time" value-format="HH:mm:ss"></el-time-picker>
                    </el-form-item>
                </el-form>
            </template>

            <template #footer>
                <el-button type="primary" @click="submit()">提交</el-button>
                <el-button @click="cancel()">取消</el-button>
            </template>
        </el-drawer>


        <h1>已通过</h1>
        <el-table :data="user_pass_info" stripe border>
            <el-table-column prop="user_name" label="姓名" />
            <el-table-column prop="user_num" label="学号" />
            <el-table-column prop="car_name" label="车牌号" />
            <el-table-column prop="car_start_time" label="开始时间" />
            <el-table-column prop="car_end_time" label="结束时间" />
        </el-table>
    </div>
</template>

<script>
import axios from "axios"

export default {
    name: "UserAdmin",
    data() {
        return {
            // 是否显示抽屉
            drawer: false,

            // 用户在抽屉中填写的表单
            car_info: {
                for_user_num: "183424080320",
                car_name: "",
                car_start_time: "",
                car_end_time: "",
                car_is_pass: "0"
            },
            start_date: "",
            start_time: "",
            end_date: "",
            end_time: "",

            // 已通过的数据
            user_nopass_info: [],
            // 未通过的数据
            user_pass_info: []
        }
    },

    methods: {
        onDel(index) {
            console.log(index);
        },

        submit() {
            this.car_info.car_start_time = this.start_date + " " + this.start_time;
            this.car_info.car_end_time = this.end_date + " " + this.end_time;

            axios
                .post("http://192.168.0.111:8000/user/car/add", this.car_info)
                .then(res => {
                    console.log(res);
                })
                .catch(err => {
                    console.log(err);
                });

            this.cancel();
            // 刷新页面
            this.$router.go(0);
        },

        cancel() {
            this.drawer = false;
        }
    },

    mounted() {
        axios
            .get("http://192.168.0.111:8000/user/info/?ispass=0&user_num=183424080320")
            .then(res => {
                this.user_nopass_info = JSON.parse(res.data);
                // console.log(res.data);
            })
            .catch(err => {
                console.log(err);
            });

        axios
            .get("http://192.168.0.111:8000/user/info/?ispass=1&user_num=183424080320")
            .then(res => {
                // console.log(res);
                this.user_pass_info = JSON.parse(res.data);
                // console.log(res.data);
            })
            .catch(err => {
                console.log(err);
            });
    }
}
</script>

<style scoped>

</style>
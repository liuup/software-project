<template>
    <div class="userregister">
        <el-form
            label-position="top"
            :model="user_register_form"
        >
            <el-form-item label="姓名">
                <el-input v-model="user_register_form.user_name"></el-input>
            </el-form-item>
            <el-form-item label="学号">
                <el-input v-model="user_register_form.user_num"></el-input>
            </el-form-item>
            <el-form-item label="密码">
                <el-input v-model="user_register_form.user_pwd" type="password" ></el-input>
            </el-form-item>
            <el-form-item label="再次输入密码">
                <el-input v-model="user_pwd_again" type="password" @blur="pwd_check()"></el-input>
            </el-form-item>
        </el-form>
        <el-button type="primary" @click="submit()">Submit</el-button>
        <el-button @click="reset()">Reset</el-button>
    </div>
</template>

<script>
import { ElMessage } from 'element-plus'

export default {
    name: "UserRegiter",
    data() {
        return {
            user_register_form: {
                user_name: "",
                user_num: "",
                user_pwd: ""
            },
            user_pwd_again: ""

        }
    },

    methods: {
        // 密码校验
        pwd_check() {
            if(this.user_register_form.user_pwd != this.user_pwd_again) {
                ElMessage.error("密码不匹配");
            }
        },

        // 注册表单提交处理
        submit() {
            if(this.user_register_form.user_name == "" ||
                this.user_register_form.user_num == "" ||
                this.user_register_form.user_pwd == "" ||
                this.user_pwd_again == "") {

                ElMessage.error("输入禁止为空");
                this.reset();
                return
            }

            // TODO: 处理提交post逻辑


        },

        // 表单重置
        reset() {
            this.user_register_form.user_name = "";
            this.user_register_form.user_num = "";
            this.user_register_form.user_pwd = "";
            this.user_pwd_again = "";
        }
    }


}
</script>

<style scoped>

</style>
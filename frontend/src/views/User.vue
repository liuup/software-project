<template>
  <div class="user">
    <el-image :src="img_url"></el-image>
    
    <el-form
      label-position="top"
      :model="loginForm"
    >
      <el-form-item label="用户学号">
        <el-input v-model="loginForm.user_num" clearable></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="loginForm.user_pwd" type="password" show-password></el-input>
      </el-form-item>

    </el-form>

    <el-button type="primary" @click="login()">登录</el-button>
    <el-button @click="cancel()">清空</el-button>
    <el-button type="info" plain @click="register()">注册</el-button>

    <!-- <el-table :data="testusers" border stripe>
      <el-table-column prop="user_num" label="测试学号"/>
      <el-table-column prop="user_pwd" label="测试密码"/>
    </el-table> -->
  </div>
</template>

<script>
import { ref } from "vue"
import axios from "axios"
import { ElMessage } from "element-plus";

export default {
  name: 'User',
  data() {
    return {
      img_url: "https://api.multiavatar.com/6a9128b7c6947fe71b.svg",

      loginForm: {
        user_num: "", // 用户学号
        user_pwd: ""  // 用户密码
      },

      testusers: [
        {"user_num": "183424080320", "user_pwd": "123"},
        {"user_num": "183406010501", "user_pwd": "456"},
        {"user_num": "183408020114", "user_pwd": "789"},
      ]
    }
  },
  methods: {
    // 登录方法
    login() {
      if(this.loginForm.user_num == "" || this.loginForm.user_pwd == "") {
        ElMessage.error("禁止输入为空");
        this.cancel();
        return
      }

      axios
        .post('http://192.168.0.111:8000/user/login', this.loginForm)
        .then(res => {
          this.data = JSON.parse(res.data)

          if(this.data.status == "failure") {
            ElMessage.error("账号或密码错误");
          } else if(this.data.status == "successful") {
            ElMessage.success("登录成功");
            this.$router.push({path: "/user/admin"});  // 跳转到用户管理路由
          }
        })
        .catch(err => {
          console.log(err);
        });

      this.cancel(); // 清空输入框
    },

    // 清除方法
    cancel() {
      this.loginForm.user_num = "";
      this.loginForm.user_pwd = "";
    },

    // 注册方法
    register() {
      console.log("register function");
      this.$router.push({path: "/user/register"});  // 跳转到用户注册路由
    }
  }
}
</script>

<style>
.el-sk-item {
  width: 300px;
  height: 300px;
  text-align: center;
}

</style>
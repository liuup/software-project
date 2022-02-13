<template>
  <div class="guard">
    <el-image :src="img_url"></el-image>

    <el-form
      label-position="top"
      :model="loginForm"
    >
      <el-form-item label="保安工号">
        <el-input v-model="loginForm.guard_num" clearable></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="loginForm.guard_pwd" type="password" show-password></el-input>
      </el-form-item>

    </el-form>

    <el-button type="primary" @click="login()">登录</el-button>
    <el-button @click="cancel()">清空</el-button>
    
    <el-table :data="testguards" border stripe>
      <el-table-column prop="guard_num" label="测试工号"/>
      <el-table-column prop="guard_pwd" label="测试密码"/>
    </el-table>
  </div>
</template>


<script>
import axios from "axios"
import { ElMessage } from "element-plus";

export default {
  name: "Guard",
  data() {
    return {
      img_url: "https://api.multiavatar.com/d6463fcebcd1033da0.svg",

      loginForm: {
        guard_num: "",
        guard_pwd: ""
      },
      testguards: [
        {"guard_num": "2022001", "guard_pwd": "1234"},
        {"guard_num": "2022002", "guard_pwd": "7890"},
      ]

    }
  },
  methods: {
    login() {
      if(this.loginForm.guard_num == "" || this.loginForm.guard_pwd == "") {
        ElMessage.error("禁止输入为空");
        this.cancel();
        return
      }

      axios
        .post('http://192.168.0.111:8000/guard/login', this.loginForm)
        .then(res => {
          this.data = JSON.parse(res.data)

          if(this.data.status == "failure") {
            ElMessage.error("账号或密码错误");
          } else if(this.data.status == "successful") {
            ElMessage.success("登录成功");
            this.$router.push({path: "/guard/admin"});  // 跳转到管理路由
          }
        })
        .catch(err => {
          console.log(err);
        });

      this.cancel(); // 清空输入框
    },
    cancel() {
      this.loginForm.guard_num = "";
      this.loginForm.guard_pwd = "";
    }

  }
}


</script>


<style>


</style>

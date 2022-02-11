<template>
  <div class="guard">
    <el-image :src="img_url"></el-image>

    <el-form
      :label-position="labelPosition"
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
  </div>
</template>


<script>
import { ref } from "vue"
import axios from "axios"
import { ElMessage } from "element-plus";

export default {
  name: "Guard",
  data() {
    return {
      img_url: "https://avataaars.io/?avatarStyle=Circle&topType=LongHairFrida&accessoriesType=Prescription01&facialHairType=MoustacheFancy&facialHairColor=Black&clotheType=BlazerShirt&clotheColor=Gray01&eyeType=Wink&eyebrowType=SadConcerned&mouthType=Grimace&skinColor=Pale",
      
      labelPosition: ref("top"),
      loginForm: {
        guard_num: "",
        guard_pwd: ""
      }
    }
  },
  methods: {
    login() {
      console.log("login func");

      axios
      .post('http://192.168.0.111:8000/guard/login', this.loginForm)
      .then(res => {
        this.data = JSON.parse(res.data)

        if(this.data.status == "failure") {
          ElMessage.error("账号或密码错误");
        } else if(this.data.status == "successful") {
          ElMessage.success("登录成功");
        }
      })
      .catch(err => {
        console.log(err);
      });

      this.cancel(); // 清空输入框
    },
    cancel() {
      console.log("cancel func");
      this.loginForm.guard_num = "";
      this.loginForm.guard_pwd = "";

    }

  }
}


</script>


<style>


</style>
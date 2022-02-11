<template>
  <div class="user">
    <el-image :src="img_url"></el-image>
    
    <el-form
      :label-position="labelPosition"
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
      img_url: "https://avataaars.io/?avatarStyle=Circle&topType=ShortHairShortCurly&accessoriesType=Prescription02&hatColor=Blue02&hairColor=BlondeGolden&facialHairType=BeardMedium&facialHairColor=BlondeGolden&clotheType=GraphicShirt&clotheColor=Gray02&graphicType=Bear&eyeType=Side&eyebrowType=FlatNatural&mouthType=Smile&skinColor=Pale",
      
      labelPosition: ref("top"),
      loginForm: {
        user_num: "", // 用户学号
        user_pwd: ""  // 用户密码
      },
      data: {}
    }
  },
  methods: {
    // 登录方法
    login() {
      axios
      .post('http://192.168.0.111:8000/user/login', this.loginForm)
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

    // 清除方法
    cancel() {
      this.loginForm.user_num = "";
      this.loginForm.user_pwd = "";
      // console.log("cancel function");
    },

    // 注册方法
    register() {
      console.log("register function");
      // TODO: 补全
    }


  }
}
</script>

<style>
el-link {
  padding: 50px;
}

.el-sk-item {
  width: 300px;
  height: 300px;
  text-align: center;
}
</style>
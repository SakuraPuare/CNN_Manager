<script lang="ts" setup>
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faCloud } from "@fortawesome/free-solid-svg-icons";
import {
  genFileId,
  UploadInstance,
  UploadProps,
  UploadRawFile,
  UploadRequestHandler,
} from "element-plus";
import { ref } from "vue";
import { postImageAPI } from "@/apis/image";
import { postImageParams, postImageResponse } from "@/types/image";

const props = defineProps<{
  limit: number;
}>();
const emits = defineEmits(["uploadSuccess"]);

const uploadFile = ref<UploadInstance>();

const onUpload: UploadRequestHandler = (option) => {
  const params: postImageParams = { file: option.file };
  return postImageAPI(params);
};

const onFileExceed: UploadProps["onExceed"] = (files) => {
  uploadFile.value!.clearFiles();
  const file = files[0] as UploadRawFile;
  file.uid = genFileId();
  uploadFile.value!.handleStart(file);
};

const onUploadSuccess = (response: postImageResponse) => {
  emits("uploadSuccess", response);
};
</script>

<template>
  <el-upload
    ref="uploadFile"
    :http-request="onUpload"
    :limit="props.limit || 1"
    :on-exceed="onFileExceed"
    :on-success="onUploadSuccess"
    class="w-full"
    drag
    list-type="picture"
    multiple
  >
    <el-icon class="el-icon--upload">
      <font-awesome-icon :icon="faCloud" />
    </el-icon>
    <div class="el-upload__text">
      Drop file here or <em>click to upload</em>
    </div>
    <template #tip>
      <div class="el-upload__tip">
        jpg/png files with a size less than 500kb
      </div>
    </template>
  </el-upload>
</template>

<style scoped></style>

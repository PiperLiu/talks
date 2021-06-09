# 如何使用 slidev
部分演讲投影将基于 h5 部署，使用 [slidev](https://sli.dev/) 生成。

运行 `ps` 脚本，即可生成新 `slidev` 单页面到 `talks/` 中，并且备份 `slidev` 中 `md` 配置：
```bash
./build.ps <演讲名称>
```

在 GitHub 或者 Gitee 配置时，将 {root} 配置为 page 。

### 导出 pdf

```bash
cd ./slidev

npm i -D playwright-chromium
npm run export
```

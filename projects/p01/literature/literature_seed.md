# P01 文献种子清单

本文档是 D0 阶段的文献种子清单，不是最终参考文献表。所有文献在进入 manuscript bibliography 前都必须人工核验题名、作者、期刊、年份和 DOI。

## 一、经典中尺度 SST-wind coupling 框架

1. Small, R. J., deSzoeke, S. P., Xie, S.-P., O'Neill, L., Seo, H., Song, Q., Cornillon, P., Spall, M., & Minobe, S. (2008). Air-sea interaction over ocean fronts and eddies. Dynamics of Atmospheres and Oceans, 45(3-4), 274-319. https://doi.org/10.1016/j.dynatmoce.2008.01.001

   - 用途：综述 ocean fronts / eddies 与大气边界层响应，是本项目讨论 mesoscale coupling 的基础文献。

2. Chelton, D. B., & Xie, S.-P. (2010). Coupled ocean-atmosphere interaction at oceanic mesoscales. Oceanography, 23(4), 52-69. https://doi.org/10.5670/oceanog.2010.05

   - 用途：中尺度海气耦合经典框架，可用于引出“该框架是否能延伸到亚中尺度”的科学问题。

3. O'Neill, L. W., Chelton, D. B., & Esbensen, S. K. (2010). The effects of SST-induced surface wind speed and direction gradients on midlatitude surface vorticity and divergence. Journal of Climate, 23(2), 255-281. https://doi.org/10.1175/2009JCLI2613.1

   - 用途：SST front 对 surface wind speed / direction gradients、vorticity、divergence 的影响；适合支撑 coupling coefficient 的形式选择。

4. Frenger, I., Gruber, N., Knutti, R., & Munnich, M. (2013). Imprint of Southern Ocean eddies on winds, clouds and rainfall. Nature Geoscience, 6, 608-612. https://doi.org/10.1038/ngeo1863

   - 用途：说明海洋涡旋/锋面对大气风、云和降水可产生可观测响应。

## 二、风场、风应力和海洋反馈相关文献

这些文献有助于区分“近海面风速动能”与“海洋风功输入”。本项目主变量是 SWOT wind speed 与 `0.5 U^2`，不是 `tau dot u_o`。

5. Oort, A. H., Anderson, L. A., & Peixoto, J. P. (1994). Estimates of the energy cycle of the oceans. Journal of Geophysical Research, 99(C4), 7665-7688. https://doi.org/10.1029/93JC03556

6. Wunsch, C. (1998). The work done by the wind on the oceanic general circulation. Journal of Physical Oceanography, 28(11), 2332-2340. https://doi.org/10.1175/1520-0485(1998)028<2332:TWDBTW>2.0.CO;2

7. Xu, C., Zhai, X., & Shang, X.-D. (2016). Work done by atmospheric winds on mesoscale ocean eddies. Geophysical Research Letters, 43, 12,174-12,180. https://doi.org/10.1002/2016GL071275

8. Rai, S., Hecht, M., Maltrud, M., & Aluie, H. (2021). Scale of oceanic eddy killing by wind from global satellite observations. Science Advances, 7(28), eabf4920. https://doi.org/10.1126/sciadv.abf4920

## 三、SWOT 与亚中尺度背景

9. Morrow, R., Fu, L.-L., Ardhuin, F., Benkiran, M., Chapron, B., Cosme, E., d'Ovidio, F., Farrar, J. T., Gille, S. T., Lapeyre, G., Le Traon, P.-Y., Pascual, A., Ponte, A., Qiu, B., Rascle, N., Ubelmann, C., Wang, J., & Zaron, E. D. (2019). Global observations of fine-scale ocean surface topography with the Surface Water and Ocean Topography mission. Frontiers in Marine Science, 6, 232. https://doi.org/10.3389/fmars.2019.00232

   - 用途：SWOT 任务与 fine-scale ocean surface topography 的基础介绍。

10. McWilliams, J. C. (2016). Submesoscale currents in the ocean. Proceedings of the Royal Society A, 472, 20160117. https://doi.org/10.1098/rspa.2016.0117

   - 用途：亚中尺度动力学背景，帮助解释 SST fronts、filaments、strain 与边界层响应可能相关的物理基础。

## 四、近期重点核验方向

11. 题为 "Submesoscale Air-Sea Interactions as Revealed by SWOT" 的 GRL 文章与本项目高度相关，应优先核验期刊页面、DOI、数据使用方式和 SWOT wind speed 质量控制方法。已有二级记录指向 DOI `10.1029/2025GL116017`，正式引用前必须人工确认。

12. 2023 年 SWOT science phase 之后关于 SWOT wind speed、sigma0、submesoscale SSH signals、western boundary current applications 的最新论文需要系统检索。这个方向更新很快，D0 阶段不能只依赖 AI 推荐。

## 五、建议检索关键词

- "SWOT wind speed sigma0 submesoscale air sea interaction"
- "SWOT submesoscale air sea coupling wind speed SST"
- "SWOT KaRIn SSH SST wind speed gradient"
- "Gulf Stream SST fronts wind speed gradient coupling coefficient"
- "Kuroshio Extension air sea coupling Himawari SST wind"
- "scale-dependent SST wind coupling coefficient"
- "scatterometer effective resolution SST wind coupling"
- "GOES Himawari SST fronts air sea coupling western boundary currents"
